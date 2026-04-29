# SEO_GEO — AI-Powered Content Pipeline

A multi-agent system for producing human-sounding, SEO and GEO optimized blog content for Straunt.ai. Built entirely within the Antigravity framework.

---

## How It Works

Three specialized agents work in sequence inside a single conversation to take a topic from raw idea to a publish-ready, optimized blog post.

```
You give a topic
      ↓
[Researcher] → Research Brief + content angle
      ↓
[Writer]     → Human-sounding 1,000-1,500 word draft
      ↓
[Editor]     → SEO + GEO optimized final article + meta elements
```

---

### Step 4 — Optional: Push to Google Docs
After you've reviewed the final article from the Editor and want it as a Google Doc, just type:
```
Push this to Google Docs.
```
The agent will execute the `push_to_gdocs.py` script and give you a direct link to your new document.

---

## Google Docs Setup (One-Time)

To use the **Step 4** push feature, you need to provide your own Google Cloud credentials:

1. Create a project in [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the **Google Docs API** and **Google Drive API**.
3. Create **OAuth 2.0 Client ID** credentials (Desktop app type).
4. Download the JSON file, rename it to `credentials.json`, and place it in the `SEO_GEO/` folder.
5. The first time you run the push, follow the browser login prompt. A `token.json` will be saved for future use.

---

## Folder Structure

```
SEO_GEO/
├── README.md                          ← You are here
│
├── agents/                            ← The three agent instruction files
│   ├── researcher/SKILL.md            ← Keyword research, competitor analysis, content brief
│   ├── writer/SKILL.md                ← Human-first draft using frameworks + voice rules
│   └── editor/SKILL.md                ← SEO + GEO optimization pass
│
├── skills/                            ← Shared knowledge modules loaded by agents
│   ├── writing_principles/
│   │   └── humanization.md            ← Banned words, plain English dictionary, natural transitions
│   ├── frameworks/
│   │   ├── blog_framework.md          ← 7 blog post templates (Informational, How-To, Listicle, etc.)
│   │   └── title_formulas.md          ← 12 proven headline formula patterns
│   └── optimization/
│       ├── seo_best_practices.md      ← On-page SEO checklist + content template
│       ├── ai_citation_patterns.md    ← How Google AI, ChatGPT, Perplexity, Claude cite content
│       └── geo_best_practices.md      ← GEO techniques + before/after examples + quotability test
│
└── knowledge base/                    ← Straunt.ai company context (brand, keywords, competitors)
```

---

## How to Run the Pipeline

### Step 1 — Researcher
Open a new chat and type:
```
Use the skill at agents/researcher/SKILL.md

I want to write a blog post about: [YOUR TOPIC]
```
You will receive a Research Brief with keywords, competitor analysis, content gaps, and 2-3 angle options. Reply with your chosen angle to continue.

---

### Step 2 — Writer
In the same conversation, type:
```
Use the skill at agents/writer/SKILL.md

Use the Research Brief above as your input. Write the blog post draft now.
```
You will receive 3 title options and a 1,000-1,500 word human-first draft. Review the tone and give feedback if needed before moving on.

---

### Step 3 — Editor
In the same conversation, type:
```
Use the skill at agents/editor/SKILL.md

Optimize the draft above for SEO and GEO. Use the Research Brief keywords as your target.
```
You will receive the fully optimized article, meta title, meta description, and a Quotability Score out of 10. A score of 8+ means it is ready to publish.

> **Important**: Always run all three agents in one continuous conversation. Each agent needs the previous agent's output as context.

---

## What Each Skill Module Does

| File | Purpose |
|------|---------|
| `humanization.md` | Stops the AI from sounding like an AI. Bans specific words, enforces sentence variation, provides a 300+ word Plain English dictionary, and supplies natural transition phrases. |
| `blog_framework.md` | Provides structural blueprints for 7 blog post types so the Writer always uses the right format for the keyword intent. |
| `title_formulas.md` | 12 proven headline formulas with examples and a Title Writing Checklist for every piece of content. |
| `seo_best_practices.md` | On-page SEO checklist covering keyword placement, meta tag specs, readability, featured snippet patterns, and a full content template. |
| `ai_citation_patterns.md` | Explains exactly how Google AI Overviews, ChatGPT, Perplexity, and Claude select and cite content — the foundation of the GEO strategy. |
| `geo_best_practices.md` | 6 GEO optimization techniques with before/after scored examples and a 10-question Quotability Test to benchmark every article before publishing. |

---

## Content Standards

- **Word count**: 1,000–1,500 words (default for blog posts)
- **Meta title**: 50-60 characters
- **Meta description**: 150-160 characters
- **Quotability score**: 8/10 minimum before publishing
- **Voice**: Straunt.ai brand voice as defined in `knowledge base/`
