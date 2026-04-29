---
name: researching-content
description: Performs the first step of any content project. Reads the knowledge base for brand context and keywords, analyzes competitors to find content gaps, recommends the appropriate blog post type from the frameworks library, and outputs a structured research brief for the Writer agent.
---

# Content Research Skill

## When to Use This Skill
- At the very start of any new content project, before writing a single word.
- When you need to identify target keywords, analyze competitors, find content gaps, and determine the right content format before briefing the Writer.

---

## Workflow

- [ ] 1. **Load Brand Context (Knowledge Base)**
  - Read the relevant documents inside the `knowledge_base/` folder.
  - Extract: brand voice, target audience, core product positioning, and any stated SEO keyword strategies.
  - Do not perform external keyword research at this stage. Pull only from what is documented.

- [ ] 2. **Identify Target Keywords**
  - From the `knowledge_base/`, extract the primary keyword and relevant secondary/LSI keywords for the requested topic.
  - Categorize each keyword by search intent: informational, commercial, or transactional.

- [ ] 3. **Competitor Discovery**
  - Using the `knowledge_base/` competitor documents or web search, identify 2-3 competitors currently ranking for the target keyword.
  - Summarize what their content covers, how long it is, and what format they use.

- [ ] 4. **Identify Content Gaps**
  - Analyze competitor content to find what is missing: unanswered questions, shallow sections, outdated data, missing formats (e.g., no FAQ, no comparison table), or poor structure.
  - This is the most important step. The gap is our competitive edge.

- [ ] 5. **Recommend Content Type**
  - Based on the keyword intent and content gaps identified, recommend the most suitable blog post format from `frameworks/blog_framework.md`.
  - Options: Informational, Comparison, Listicle, How-To, Product Review, Pillar Page, or FAQ Page.
  - State clearly which format you recommend and why.

- [ ] 6. **Compile the Research Brief**
  - Package all findings into a structured brief for the Writer agent to act on.
  - End by asking the user which direction or angle to write about.

---

## Instructions
- Follow the workflow steps in order. Do not skip steps.
- Be specific about gaps. Vague gap analysis ("they didn't cover X well") is not useful. State exactly what is missing and what we should say instead.
- Do not suggest content angles that are not supported by the knowledge base or research.

---

## Output Format

Present the Research Brief in this exact structure:

---

### Research Brief

#### 1. Brand & Audience Context
- **Brand**: [What Straunt.ai does / key positioning]
- **Target Audience**: [Who this content is for]
- **Tone**: [Voice notes from knowledge base]

#### 2. Target Keywords
- **Primary Keyword**: [Keyword] — Intent: [Informational / Commercial / Transactional]
- **Secondary Keywords**: [Keyword 1], [Keyword 2], [Keyword 3]

#### 3. Competitors Identified
- **[Competitor A]**: [URL] — [Format, word count estimate, what they cover]
- **[Competitor B]**: [URL] — [Format, word count estimate, what they cover]

#### 4. Content Gaps & Our Edge
- **Gap 1**: [Specific missing information or weak point in competitor content]
- **Gap 2**: [Another gap]
- **Our Edge**: [Exactly how we fill these gaps and what makes our content superior]

#### 5. Recommended Content Type
- **Format**: [e.g., How-To Guide / Listicle / Informational Blog Post]
- **Why**: [One sentence justification based on keyword intent and gaps]

#### 6. Suggested Angles
1. **[Direction 1]**: [One-line description of this content angle]
2. **[Direction 2]**: [One-line description]
3. **[Direction 3]**: [One-line description]

---
*Which of these angles would you like the Writer to focus on?*
