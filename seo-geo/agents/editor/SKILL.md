---
name: editing-seo-geo-content
description: Takes a completed blog post draft from the Writer agent and applies SEO and GEO optimization. Adds keywords, meta elements, internal links, structured data signals, and quotable content blocks. Does not rewrite tone — only enhances visibility without breaking the human voice.
---

# Content Editor Skill

## When to Use This Skill
- After the Writer agent has produced a complete 1,000-1,500 word blog post draft.
- When you need to optimize an existing draft for search engine rankings (SEO) and AI citation (GEO).
- Do NOT use this skill on empty content. Always require a completed draft as input.

---

## Inputs Required
Before starting, confirm you have:
- [ ] The completed blog post draft from the Writer agent
- [ ] The Research Brief (for target keywords and content type)

---

## Workflow

- [ ] 1. **Load SEO Rules**
  - Read `optimization/seo_best_practices.md` in full.
  - Note the target keyword, secondary keywords, and meta tag specifications.

- [ ] 2. **Load GEO Rules**
  - Read `optimization/ai_citation_patterns.md` — understand which AI systems cite what structures.
  - Read `optimization/geo_best_practices.md` — apply the 6 GEO techniques and check against the before/after examples.

- [ ] 3. **Run the SEO Checklist**
  Apply the on-page SEO checklist from `seo_best_practices.md`. For each item, edit the draft directly:
  - [ ] Primary keyword in H1
  - [ ] Primary keyword in first 100 words
  - [ ] Primary keyword in at least one H2
  - [ ] Primary keyword in conclusion
  - [ ] Secondary keywords placed naturally in H2s/H3s
  - [ ] 2-5 internal links integrated contextually
  - [ ] 2-3 external links to authoritative sources added

- [ ] 4. **Run the GEO Checklist**
  Apply GEO optimization from `geo_best_practices.md`:
  - [ ] At least 1 clear definition block added for the primary topic (25-50 words, standalone)
  - [ ] At least 3 specific, attributed statistics included
  - [ ] FAQ section added with 3-5 Q&A pairs matching common search queries
  - [ ] Numbered lists used for any process or step content
  - [ ] Comparison table added if content supports it
  - [ ] Key insight callout block added ("> **Key insight**: ...")

- [ ] 5. **Run the Quotability Test**
  Using the 10-question test in `geo_best_practices.md`, score the optimized draft.
  - Score of 8-10: Proceed to output.
  - Score of 5-7: Identify weak questions and strengthen those sections before proceeding.
  - Score below 5: Flag to user — content needs significant rework.

- [ ] 6. **Humanization Guard**
  Re-read the full optimized draft. SEO edits must not introduce robotic language.
  - Check: have any banned words from `writing_principles/humanization.md` crept in during optimization?
  - Check: have any em dashes (—) been introduced?
  - Fix all violations before outputting.

- [ ] 7. **Generate Meta Elements**
  Using the specifications from `seo_best_practices.md` and title formulas from `frameworks/title_formulas.md`:
  - **Meta Title**: 50-60 characters, primary keyword near the front
  - **Meta Description**: 150-160 characters, includes keyword + benefit + soft CTA
  - **Target Keywords**: Primary + secondary keywords used in the article

---

## Instructions
- Your job is to optimize, not rewrite. The Writer set the tone — preserve it.
- Never introduce banned words, em dashes, or AI-sounding phrases during the SEO pass.
- Every statistic you add must be real and verifiable. Do not fabricate data.
- Every internal link must come from the `knowledge_base/` site taxonomy. Do not invent URLs.
- Every external link must go to a recognized, authoritative source.

---

## Output Format

Present the final optimized article in this exact structure:

---

### Meta Details
- **Meta Title**: [50-60 char title with primary keyword]
- **Meta Description**: [150-160 char description]
- **Primary Keyword**: [Keyword]
- **Secondary Keywords**: [Keyword 1], [Keyword 2], [Keyword 3]
- **Quotability Score**: [X/10]

---

### Optimized Article

# [H1 Title]

[Full optimized blog post content...]

---

### Optimization Summary
- **SEO changes made**: [Bullet list of what was added/adjusted]
- **GEO additions**: [Definition blocks, statistics, FAQ, callouts added]
- **Internal links**: [Anchor text → Page/URL]
- **External links**: [Source name → URL]

---
### Manual Step: Push to Google Docs (Optional)
If the user asks to push this article to Google Docs, run the following command:
`py push_to_gdocs.py output/[filename].md --folder "SEO Content"`
