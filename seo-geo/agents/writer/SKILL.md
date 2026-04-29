---
name: writing-blog-content
description: Writes a human-sounding, 1,000-1,500 word blog post draft based on a Research Brief. Focuses entirely on tone, structure, and readability — no SEO optimization. The Editor agent handles optimization in the next pass.
---

# Blog Content Writer Skill

## When to Use This Skill
- After the Researcher agent has produced a Research Brief and the user has confirmed a content angle.
- When you need to draft a blog post that sounds genuinely human and follows the correct structural framework.
- Do NOT use this skill without a Research Brief. Always require the brief as input.

---

## Inputs Required
Before starting, confirm you have:
- [ ] The Research Brief from the Researcher agent (keywords, angle, recommended content type)
- [ ] The confirmed content angle from the user

---

## Workflow

- [ ] 1. **Load Writing Rules**
  - Read `writing_principles/humanization.md` in full before writing a single word.
  - These rules are non-negotiable. Every sentence must pass the humanization standard.
  - Pay particular attention to: banned vocabulary, natural transitions, sentence length variation, and the Plain English dictionary.

- [ ] 2. **Load the Correct Framework**
  - Read `frameworks/blog_framework.md` and select the section matching the content type recommended in the Research Brief (e.g., How-To, Informational, Listicle).
  - Use that framework's structure as the skeleton for the draft.

- [ ] 3. **Load Title Formulas**
  - Read `frameworks/title_formulas.md`.
  - Generate 3 title options using different formula patterns. Present these to the user before drafting if possible, or include them at the top of the output.

- [ ] 4. **Load Brand Context**
  - Read relevant documents in `knowledge_base/` to absorb the Straunt brand voice, product positioning, and audience.
  - The draft must sound like Straunt wrote it — not like a generic AI blog.

- [ ] 5. **Draft the Content**
  - Write the full blog post draft: **1,000 to 1,500 words** (default).
  - Follow the framework structure from Step 2.
  - Apply every humanization rule from Step 1. Do not use banned words or phrases.
  - Use natural transitions from the `humanization.md` signposting section.
  - Focus entirely on tone, readability, and structure. Do NOT try to optimize for SEO during this step — that is the Editor's job.
  - Integrate 2-4 internal links from the `knowledge_base/` site taxonomy where they fit naturally. Never fabricate links.

- [ ] 6. **Self-Check Before Output**
  - Re-read the draft and flag any sentences that:
    - Use a banned word or phrase from `humanization.md`
    - Use an em dash (—) more than once
    - Sound like they were written by an AI
  - Fix all flagged items before outputting.

---

## Instructions
- Tone is the priority of this draft. SEO comes later.
- Word count must be between 1,000 and 1,500 words. Do not go under or over without explicit instruction.
- Do not invent internal links, statistics, or quotes. Only use what is in the knowledge base or Research Brief.
- Use varied sentence lengths. Short ones land hard. Longer ones give context and build the reader's understanding as they move through the piece.

---

## Output Format

Present the draft in this exact structure:

---

### Title Options
1. [Title Option 1 — state which formula was used]
2. [Title Option 2 — state which formula was used]
3. [Title Option 3 — state which formula was used]

---

### Content Draft

*(Word count: [X] words)*

# [Chosen H1 Title]

[Full blog post body following the selected framework structure...]

---

### Internal Links Used
- [Anchor text] → [URL or page name from knowledge base]
- [Anchor text] → [URL or page name from knowledge base]

---
*Draft complete. Pass this to the Editor agent for SEO and GEO optimization.*
