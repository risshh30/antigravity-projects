#!/usr/bin/env python3
"""
push_to_gdocs.py
----------------
Pushes a markdown output file to a new Google Doc.

Usage:
    py push_to_gdocs.py output/your_file.md
    py push_to_gdocs.py output/your_file.md --folder "SEO Content"

Requirements:
    - credentials.json in the SEO_GEO root folder (from Google Cloud Console)
    - First run opens a browser for one-time OAuth approval
    - token.json is saved after first auth (do not delete it)
"""

import os
import sys
import re
import argparse
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Permissions needed: create Docs, create/read Drive folders
SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive",
]

BASE_DIR = Path(__file__).parent
CREDENTIALS_FILE = BASE_DIR / "credentials.json"
TOKEN_FILE = BASE_DIR / "token.json"


def authenticate():
    """Authenticate and return Google API credentials."""
    creds = None

    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_FILE.exists():
                print("\n❌  credentials.json not found.")
                print("    Download it from Google Cloud Console → APIs & Services → Credentials")
                print(f"    Place it at: {CREDENTIALS_FILE}\n")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return creds


def extract_title(content: str, filepath: Path) -> str:
    """Extract the H1 title from markdown, or use the filename as fallback."""
    match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if match:
        # Clean up any markdown bold/italic from title
        title = re.sub(r"[*_`]", "", match.group(1)).strip()
        return title
    return filepath.stem.replace("_", " ").replace("-", " ").title()


def parse_meta_block(content: str) -> dict:
    """Extract Meta Title and Meta Description if present."""
    meta = {}
    title_match = re.search(r"\*\*Meta Title\*\*:\s*(.+)", content)
    desc_match = re.search(r"\*\*Meta Description\*\*:\s*(.+)", content)
    if title_match:
        meta["title"] = title_match.group(1).strip()
    if desc_match:
        meta["description"] = desc_match.group(1).strip()
    return meta


def markdown_to_gdoc_requests(content: str) -> list:
    """
    Convert markdown content to a list of Google Docs API batchUpdate requests.
    Handles: H1-H3, bold, bullet lists, numbered lists, paragraphs, horizontal rules.
    """
    requests = []
    index = 1  # Google Docs text index starts at 1

    def insert_text(text, style="NORMAL_TEXT", bold=False):
        nonlocal index
        requests.append({
            "insertText": {
                "location": {"index": index},
                "text": text
            }
        })
        text_len = len(text)

        if style != "NORMAL_TEXT" or bold:
            style_request = {
                "updateParagraphStyle": {
                    "range": {
                        "startIndex": index,
                        "endIndex": index + text_len - 1
                    },
                    "paragraphStyle": {"namedStyleType": style},
                    "fields": "namedStyleType"
                }
            }
            requests.append(style_request)

        index += text_len

    lines = content.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]

        # Headings
        if line.startswith("### "):
            text = line[4:].strip() + "\n"
            insert_text(text, "HEADING_3")
        elif line.startswith("## "):
            text = line[3:].strip() + "\n"
            insert_text(text, "HEADING_2")
        elif line.startswith("# "):
            text = line[2:].strip() + "\n"
            insert_text(text, "HEADING_1")

        # Horizontal rule → blank line
        elif line.strip() in ("---", "***", "___"):
            insert_text("\n")

        # Bullet list items
        elif line.startswith("- ") or line.startswith("* "):
            text = re.sub(r"\*\*(.+?)\*\*", r"\1", line[2:]).strip() + "\n"
            insert_text(text)

        # Numbered list items
        elif re.match(r"^\d+\.\s", line):
            text = re.sub(r"^\d+\.\s", "", line)
            text = re.sub(r"\*\*(.+?)\*\*", r"\1", text).strip() + "\n"
            insert_text(text)

        # Blockquote
        elif line.startswith("> "):
            text = line[2:].strip() + "\n"
            insert_text(text)

        # Empty line
        elif line.strip() == "":
            insert_text("\n")

        # Normal paragraph
        else:
            # Strip inline markdown formatting for plain text
            text = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
            text = re.sub(r"\*(.+?)\*", r"\1", text)
            text = re.sub(r"`(.+?)`", r"\1", text)
            text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
            insert_text(text.strip() + "\n")

        i += 1

    return requests


def get_or_create_folder(drive_service, folder_name: str) -> str:
    """Get Drive folder ID by name, create it if it doesn't exist."""
    query = f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}' and trashed=false"
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    folders = results.get("files", [])

    if folders:
        return folders[0]["id"]

    # Create folder
    folder_metadata = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder"
    }
    folder = drive_service.files().create(body=folder_metadata, fields="id").execute()
    return folder["id"]


def push_to_gdocs(filepath: str, folder_name: str = None):
    """Main function: read file and push to a new Google Doc."""
    path = Path(filepath)

    if not path.exists():
        print(f"\n❌  File not found: {filepath}\n")
        sys.exit(1)

    print(f"\n📄  Reading: {path.name}")
    content = path.read_text(encoding="utf-8")

    # Get title
    meta = parse_meta_block(content)
    doc_title = meta.get("title") or extract_title(content, path)
    print(f"📝  Doc title: {doc_title}")

    # Authenticate
    print("🔐  Authenticating with Google...")
    creds = authenticate()
    docs_service = build("docs", "v1", credentials=creds)
    drive_service = build("drive", "v3", credentials=creds)

    # Create blank Google Doc
    print("📁  Creating Google Doc...")
    doc = docs_service.documents().create(body={"title": doc_title}).execute()
    doc_id = doc["documentId"]

    # Build and send content requests
    print("✍️   Writing content...")
    requests = markdown_to_gdoc_requests(content)
    if requests:
        docs_service.documents().batchUpdate(
            documentId=doc_id,
            body={"requests": requests}
        ).execute()

    # Move to folder if specified
    if folder_name:
        print(f"📂  Moving to folder: {folder_name}")
        folder_id = get_or_create_folder(drive_service, folder_name)
        drive_service.files().update(
            fileId=doc_id,
            addParents=folder_id,
            removeParents="root",
            fields="id, parents"
        ).execute()

    doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"
    print(f"\n✅  Done! Your Google Doc is ready:")
    print(f"    {doc_url}\n")
    return doc_url


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Push a markdown output file to a new Google Doc."
    )
    parser.add_argument("filepath", help="Path to the markdown file (e.g. output/article.md)")
    parser.add_argument(
        "--folder",
        default="SEO Content",
        help="Google Drive folder name to save the doc in (default: 'SEO Content')"
    )
    args = parser.parse_args()

    push_to_gdocs(args.filepath, args.folder)
