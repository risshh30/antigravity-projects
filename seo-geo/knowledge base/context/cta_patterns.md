# Straunt – CTA Patterns

This document catalogues every call-to-action (CTA) used across the Straunt website — including the exact copy, placement, button style, context of use, and the underlying conversion goal. Use this to maintain consistent CTA usage in all new content and pages.

---

## CTA Hierarchy

Straunt uses a clear 3-tier CTA hierarchy:

| Tier | Type | Purpose |
|------|------|---------|
| **Primary** | "Book A Demo" | Direct sales conversion — the main goal of every page |
| **Secondary** | "Explore / See More / Read More →" | Engagement / navigation deeper into the funnel |
| **Tertiary** | "Contact Us / Refer / Partner" | Non-urgent; relationship or community entry points |

---

## Tier 1: Primary CTAs (Conversion)

### "Book A Demo"
- **Copy**: `Book A Demo`
- **Variants**: `Book a Demo` / `Schedule your demo` / `Schedule a Demo`
- **Button style**: Pill-shaped (border-radius: 9999px), brand orange (`#F97A34`), white bold text
- **Placement**:
  - Sticky top-right navigation bar — **present on every single page**
  - Hero section of every solution and AI agent page
  - Mid-page section breaks on homepage
  - Footer section above the site footer
- **Goal**: Get a sales demo call booked — the primary conversion event for Straunt
- **Context examples**:
  - *"[Book A Demo](https://www.straunt.ai/book-a-demo)"* — nav bar
  - *"[Schedule your demo](https://www.straunt.ai/book-a-demo)"* — solutions page hero
  - *"[Schedule a Demo](https://www.straunt.ai/book-a-demo)"* — footer CTA block

> **Rule**: Every page on the site leads to this CTA. It never changes style, always orange pill.

---

## Tier 2: Secondary CTAs (Engagement & Navigation)

### "Explore more solutions"
- **Copy**: `Explore more solutions`
- **Button style**: Pill-shaped, orange (same as primary but used at section level)
- **Placement**: After the product module carousel on the homepage
- **Target URL**: `/solutions`
- **Goal**: Push visitors who've seen the module overview to the full solutions hub

### "See More" / "See More →"
- **Copy**: `See More`
- **Button/link style**: Text link or ghost button with directional arrow
- **Placement**:
  - Below AI agents section ("AI Agents Help Restaurants... [See More]")
  - Below solutions nav dropdown
- **Target URLs**: `/ai-agents`, `/solutions`
- **Goal**: Drive exploration without high-commitment demand

### "Read More →"
- **Copy**: `Read More →`
- **Style**: Text link with arrow (`→`), no button background
- **Placement**: Inside product module cards on the homepage (each solution card has this link)
- **Target pages**:
  - Straunt Direct → `/straunt-direct`
  - Straunt Loyalty → `/straunt-loyalty`
  - Straunt Campaigns → `/straunt-campaigns`
  - Straunt Reviews → `/straunt-reviews`
  - Straunt Connect → `/straunt-connect`
  - Straunt Ops → `/straunt-ops`
  - Straunt Dash → `/straunt-dash`
  - Straunt POS → `/straunt-pos`
  - AI Ordering → `/ai-order-taking`
  - AI Reservation → agent marketplace URL
  - AI Marketer → `/ai-marketer`
- **Goal**: Drive click-through from homepage cards to individual product pages

### "Explore more AI agents"
- **Copy**: `Explore more AI agents`
- **Style**: Text link
- **Placement**: Bottom of `/straunt-ai` page after the 3 agent descriptions
- **Target URL**: `/straunt-ai` or `/ai-agents`
- **Goal**: Encourage exploration of the full agent marketplace

---

## Tier 3: Tertiary CTAs (Community / Relationship)

### "Become a Partner"
- **Copy**: `Become a Partner`
- **Style**: Text link in Resources navigation dropdown and footer
- **Target URL**: `/become-a-partner`
- **Goal**: Partner/reseller program sign-up for agencies and consultants

### "Refer a Business"
- **Copy**: `Refer a Business`
- **Style**: Text link in Resources navigation and footer
- **Target URL**: `/refer-a-business`
- **Goal**: Activate existing restaurant customers to refer other restaurants; growth loop

### "Contact Us"
- **Copy**: `Contact Us`
- **Style**: Text link in Resources navigation and footer
- **Target URL**: `/contact-us`
- **Goal**: Low-barrier entry point for prospects who aren't ready to book a demo

---

## Page-Level CTA Patterns (by template)

### Homepage Pattern
```
[Hero CTA]        → "Book A Demo" (orange pill, center/left)
[Solution cards]  → "Read More →" (text links per card)
[Solutions CTA]   → "Explore more solutions" (orange pill)
[AI agents]       → "See More" (text link)
[Demo block]      → "Book A Demo" (orange pill, repeated)
[Footer CTA]      → "Schedule a Demo" (orange pill)
```

### Solution Page Pattern (e.g., /straunt-dash, /straunt-direct)
```
[Hero]            → "Book A Demo" or "Schedule your demo" (orange pill)
[How it works]    → No CTA (informational section)
[Impact stats]    → No CTA (proof section)
[Testimonials]    → No CTA (social proof)
[FAQ]             → No CTA
[Footer block]    → "See how modern restaurants run..." + "Schedule a Demo"
```

### AI Agent Page Pattern (e.g., /ai-order-taking)
```
[Hero]            → "Book A Demo" (orange pill)
[Agent features]  → No inline CTA
[Results section] → No CTA
[Footer block]    → "Schedule a Demo" (orange pill)
```

---

## CTA Copy Patterns & Rules

### Language Rules
1. **Always an action verb**: Book, Schedule, Explore, See, Read
2. **Never passive or weak**: No "Learn More," "Click Here," "Get Started," "Sign Up"
3. **"Book" vs "Schedule"**: Both are used interchangeably for the demo CTA — "Book A Demo" more common in nav/hero; "Schedule a Demo" more common in footer/in-page
4. **Arrow (`→`)**: Used exclusively on text links, never on pill buttons
5. **Capitalization**: Title case for pill buttons; sentence case for text links (e.g., "Read More →" vs "Explore more solutions")

### What Straunt Does NOT Do
- ❌ No free trial CTA
- ❌ No "Sign Up Free" button
- ❌ No "Get a Quote" button
- ❌ No "Start for Free" — all demos are gated through Book A Demo
- ❌ No chat widget CTA (not observed)
- ❌ No email capture / newsletter sign-up popups

---

## CTA Context: Problem → Solution → CTA Flow

Straunt consistently uses this 3-step flow before a CTA:

1. **State the problem** (1 line, in the operator's language)
2. **Introduce the solution** (1–2 lines describing the Straunt feature)
3. **CTA** (Book A Demo)

**Example** (from homepage):
> *"Missed call = missed revenue. You not only miss the current sale but all the future sales from that person."*
> *"Straunt AI order taking ensures the phone gets picked up every time and upsells happen consistently."*
> **[Book A Demo]**

---

## Frequently Used CTA Anchor Text (for content writing)

When linking to Straunt pages from blog posts or articles, use these CTA anchor texts:

| Destination Page | Recommended Anchor Text |
|-----------------|------------------------|
| `/book-a-demo` | "Book a Demo," "Schedule a Demo," "See Straunt in action" |
| `/straunt-ai` | "Straunt AI," "try AI phone answering," "see how the AI works" |
| `/straunt-dash` | "Straunt Dash," "manage all your delivery apps in one place" |
| `/straunt-direct` | "Straunt Direct," "start taking commission-free orders" |
| `/straunt-loyalty` | "Straunt Loyalty," "build a restaurant loyalty program" |
| `/straunt-reviews` | "Straunt Reviews," "automate your review collection" |
| `/straunt-campaigns` | "Straunt Campaigns," "send automated campaigns" |
| `/solutions` | "explore all Straunt solutions," "see the full platform" |
