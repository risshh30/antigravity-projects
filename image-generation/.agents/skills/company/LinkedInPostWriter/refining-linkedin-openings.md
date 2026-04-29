---
name: refining-linkedin-openings
description: Refines the opening of a LinkedIn post when the user wants a stronger start without using flashy, misleading, or overly formulaic hooks. It first understands the topic, audience psyche, and desired tone, then asks how the user wants the post to begin and lightly improves that opening for clarity, relevance, and engagement.
---

# LinkedIn Hook Refinement

## When to use this skill
- The user has a topic and wants help shaping the beginning of a LinkedIn post.
- The user has a **Post Framework** or **Content Plan** and wants to refine the hook for a specific branch.
- The user does not want prebuilt hook formulas or exaggerated opening lines.
- The user wants the post opening to feel natural, relevant, and specific to the topic.
- The user wants a LinkedIn start that is stronger, but still honest and non-clickbait.
- The user already has an idea of how the post should begin and wants it refined.

## Core principle
This skill does not rely on stock hook templates or pre-written opening patterns.

It first understands:
- What topic the post is about.
- Who the post is for.
- What the audience is likely thinking, fearing, wanting, or resisting.
- How the user wants the post to start.

Only after that does it refine the opening to make it more:
- Relevant
- Clear
- Sharp
- Scroll-worthy
- Native to LinkedIn

The opening should never become:
- Misleading
- Sensational
- Overpromised
- Needlessly dramatic
- Generic engagement bait

## Workflow

### PLAN: Understand the post before writing the opening
Gather or infer these inputs:

1. Topic
- What is the actual subject of the post? (Inherit from **Content Plan** or **Post Brief** if available).
- Is it a story, opinion, lesson, framework, observation, or case study?

2. Audience
- Who is this for? (Inherit from **ICP** in the context or `knowledge_company/positioning/icp.md`).
- What role, level, industry, or type of person is meant to connect with it?

3. Audience psyche
Identify:
- What this audience cares about most in relation to the topic.
- What tension, frustration, curiosity, fear, or aspiration may be present.

**0. Research Brand Context**
- **Consult `knowledge_company/brand/brand_voice.md`** to ensure the hook matches the brand's primary tone (e.g., direct vs. reflective).

4. User-preferred opening direction
Ask:
- How do you want the LinkedIn post to start?
- Do you already have a first line or rough opening in mind?
- Should it begin with a statement, observation, story moment, tension, or reflection?

If the user gives no opening direction, ask for a rough intended start before refining anything.

### VALIDATE: Check the opening direction
Before refining, verify:

- The opening connects naturally to the actual topic.
- The opening feels appropriate for the intended audience.
- The opening is not vague or empty.
- The opening does not promise something the post will not deliver.
- The tone matches the user's preference.
- The opening does not sound like recycled LinkedIn bait.

If the opening is too broad, too dramatic, or too generic, narrow it before rewriting.

### EXECUTE: Refine the opening
Take the user's intended start and improve it carefully.

Allowed improvements:
- Sharpen wording
- Improve relevance to the ICP
- Add specificity
- Reduce vagueness
- Increase clarity
- Add mild tension or curiosity where appropriate
- Improve rhythm and readability

Do not:
- Turn it into clickbait
- Add exaggerated claims
- Force a dramatic tone
- Make the line sound like a generic creator template
- Invent emotional intensity that is not present in the topic

## How to ask for input
Use short, practical questions such as:

- What is the post about?
- Who is this meant for?
- What do you want the first line or opening to sound like?
- Do you already have a rough starting line?
- Should the opening feel direct, reflective, analytical, or conversational?

Ask only what is necessary.

## Output format
Return:

1. Opening analysis
```text
Topic: ...
Audience: ...
Audience mindset: ...
Opening intention: ...
```

2. Refined opening options
Provide 3–5 options based on the user's intended start.

3. Brief notes
For each option, briefly state what was improved:
- clearer
- more specific
- better audience relevance
- less generic
- stronger but still honest

## Refinement mode
If the user provides a first line or opening paragraph:

- Keep the meaning intact.
- Preserve the user's tone unless it clearly weakens the post.
- Refine lightly, not aggressively.
- Return multiple versions with small differences in sharpness.

## Quality checklist
Before finalizing:

- The opening fits the actual topic.
- The opening matches the audience’s psychology.
- The opening sounds human and natural.
- **The opening aligns with the brand voice guidelines** in `knowledge_company/brand/brand_voice.md`.
- The opening is not flashy for the sake of being flashy.
- The opening is strong enough to earn attention without being deceptive.
- The opening feels like the beginning of this post specifically, not a generic LinkedIn post.

## Error handling
If the user asks for “better hooks” but gives no topic:
- Ask what the post is about first.

If the user gives a topic but no audience:
- Ask who the post is for, or infer a reasonable audience and state that briefly.

If the user asks for a hook but rejects formulaic writing:
- Do not generate template-style hooks.
- Ask how they want the post to begin.

If the user's proposed opening is too exaggerated:
- Tone it down while preserving the intent.
- Explain briefly that the revision improves credibility and fit.

## Resources
- Use `resources/opening-refinement-notes.md` for refinement guidance if added later.
- Use `examples/opening-revisions.md` only for internal reference if examples are added later, not as default output.