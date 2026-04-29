# Skill: LinkedIn Carousel Visual Identity System
**File:** `carousel-visual-identity.md`  
**Scope:** Applies to all LinkedIn carousel slides generated for Straunt  
**Replaces:** Any previously described visual approach that used busy backgrounds or low-contrast overlays

---

## CRITICAL RULE — Read Before Anything Else

> **You must open and visually study the images inside the `Image references/` folder BEFORE generating any design.**  
> The references are the law. Every slide you produce must feel like it belongs in the same collection as those images.  
> If you cannot explain which reference inspired your design choice, you made the wrong choice.

---

## 1. Design Philosophy — What the References Tell Us

After studying all 5 reference images, the shared DNA is:

| Principle | What the references show |
|---|---|
| **Legibility first** | Text is ALWAYS the dominant element. Never fight the background. |
| **Flat, solid backgrounds** | Most slides use flat, opaque background colors — not photos, not gradients with texture |
| **Photography as a feature element** | When photos appear, they are either (a) cropped as isolated subjects on a flat BG, or (b) given a dark/color overlay so text is readable |
| **Typographic boldness** | Headlines are very large, very heavy, and very tight. Body text is compact and well-spaced |
| **Accent color precision** | One accent color is used for highlights, pills, badges, and borders — never splashed everywhere |
| **Structural geometry** | Decorative elements are simple shapes: circles, blobs, diagonal cuts, arched panels |
| **Premium whitespace** | Slides are NOT dense or cluttered. Space is used intentionally |

---

## 2. Color System

### Straunt Brand Palette

| Token | Value | Usage |
|---|---|---|
| `--bg-primary` | `#FFFFFF` | Default slide background |
| `--bg-secondary` | `#F5F0EB` | Warm cream — used for soft-toned slides |
| `--bg-dark` | `#1A1A2E` | Deep navy — used for contrast/CTA slides |
| `--bg-accent` | `#F97A34` | Straunt Orange — used as accent-only BG (max 1 slide per carousel) |
| `--text-primary` | `#111111` | All headlines on light backgrounds |
| `--text-secondary` | `#4B5563` | All body text on light backgrounds |
| `--text-light` | `#FFFFFF` | All text on dark or orange backgrounds |
| `--accent-orange` | `#F97A34` | Highlight pill, badge, borders, underlines, CTAs |
| `--accent-soft` | `#FFE4C8` | Light orange tint for pill backgrounds |
| `--shape-grey` | `#E5E7EB` | Geometric decorative shapes |

### Contrast Rules (NON-NEGOTIABLE)

- **Light BG + Dark text:** minimum contrast ratio 7:1 → Use `#111111` text on `#FFFFFF` or `#F5F0EB`
- **Dark BG + Light text:** Use `#FFFFFF` text on `#1A1A2E` or `#F97A34`
- **NEVER** use dark text on a photographic background without a sufficient overlay
- **NEVER** use light text on a cream/white background

---

## 3. Typography System

### Font Stack
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
```
**Primary Font:** `Plus Jakarta Sans` — modern, geometric, highly legible (replaces Lexend for tighter editorial feel)

### Type Scale for 1080×1350px Slides

| Element | Size | Weight | Color | Notes |
|---|---|---|---|---|
| `.eyebrow` | 28px | 700 | `--accent-orange` | Uppercase badge/label above headline |
| `.headline` | 88–120px | 800 | `--text-primary` | Line-height: 1.05, letter-spacing: -3px |
| `.headline-sm` | 64–72px | 800 | `--text-primary` | For longer headlines that need to wrap |
| `.stat-number` | 180px | 800 | `--accent-orange` | Stat slides only |
| `.stat-label` | 36px | 700 | `--text-primary` | Describes the stat |
| `.body-copy` | 36–40px | 500 | `--text-secondary` | Line-height: 1.6 |
| `.caption` | 24px | 400 | `#9CA3AF` | Slide counter, attribution |
| `.logo` | 28px | 800 | `--text-primary` | Brand name stamp |

### Typography Rules
1. Headlines must be **heavy and tight** — large size, tight letter-spacing, short line-height
2. After the headline, use **one** body paragraph max — never two competing blocks of body text
3. The eyebrow badge must be **pill-shaped** with `border-radius: 99px` and distinct background
4. Never use more than 2 type sizes per slide

---

## 4. Layout Architecture

### Canvas Specification
```
Width:   1080px
Height:  1350px
Ratio:   4:5 (vertical, LinkedIn native)
```

### Safe Zone
```css
padding: 108px 120px; /* 10% horizontal, roughly 8% vertical */
```
> Note: Unlike the old 216px safe zone which was too large, these tighter margins give the design more room to breathe while keeping content away from edges.

### Slide Anatomy (Standard Text Slide)
```
┌─────────────────────────────────────┐
│  [eyebrow badge]    [slide counter] │  ← top row, same horizontal line
│                                     │
│                                     │
│  HEADLINE                           │
│  THAT IS BIG                        │  ← dominant element
│  AND BOLD                           │
│                                     │
│  Body text paragraph sits here.     │  ← supporting context
│  Short, one paragraph only.         │
│                                     │
│  ─────────────────                  │  ← optional decorative bar/shape
│                                     │
│                                     │
│                        STRAUNT      │  ← bottom right logo
└─────────────────────────────────────┘
```

### Slide Anatomy (Stat Slide)
```
┌─────────────────────────────────────┐
│  [eyebrow: LEAK #1]   [counter]     │
│                                     │
│  HEADLINE ABOUT                     │
│  THE PROBLEM         [°  graphic]   │
│                                     │
│   40–60%                            │  ← stat in accent orange, massive
│   of calls go unanswered            │
│                                     │
│  ┃ Supporting body copy here.       │  ← left-border accent bar
│  ┃ Keep to 2 lines max.             │
│                                     │
│                        STRAUNT      │
└─────────────────────────────────────┘
```

---

## 5. Background Strategy — The Core Rule

### Option A: Flat Solid Background (Default — use for 80% of slides)
```css
background-color: #FFFFFF; /* or #F5F0EB or #1A1A2E */
```
- No image whatsoever
- Add decorative geometry via CSS (circles, blobs, diagonal cuts)
- This is the PRIMARY style from all the reference images

### Option B: Photo as a Framed Feature (for cover slides only)
- The photo sits **inside a visible frame/card** on a flat background — like reference images 4 & 5 where photos are placed as cropped portraits on the slide
- The slide background itself remains flat
- The photo is decorative, the text is on the flat BG

### Option C: Full-Bleed Photo with Mandatory Overlay (use rarely, max 1 slide)
If a full-bleed photo is needed:
```css
.slide::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.0) 0%,
    rgba(0, 0, 0, 0.75) 60%,
    rgba(0, 0, 0, 0.90) 100%
  );
  z-index: 1;
}
.safe-zone { position: relative; z-index: 2; }
```
- All text must be `#FFFFFF`
- Headline must have `text-shadow: 0 2px 8px rgba(0,0,0,0.5)`
- The photo should be **minimally textured** (avoid cluttered restaurant/food scenes)

### Forbidden Backgrounds
❌ Busy abstract textures or particle effects  
❌ Dark dramatic AI images without overlay  
❌ Low-contrast backgrounds where text disappears  
❌ Gradient meshes that fight the typography  

---

## 6. Decorative Element System

Inspired by reference image 1 (srch.) and references 4–5, use these CSS-only decorative shapes:

### Accent Circle (Bottom Left or Top Right Corner)
```css
.deco-circle {
  position: absolute;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  background-color: #F5F0EB; /* or accent orange at 15% opacity */
  bottom: -120px;
  left: -80px;
  z-index: 0;
}
```

### Accent Bar (Under Headline)
```css
.accent-bar {
  width: 80px;
  height: 10px;
  background-color: #F97A34;
  border-radius: 5px;
  margin: 24px 0 32px 0;
}
```

### Left Border Callout
```css
.indent-bar {
  border-left: 10px solid #F97A34;
  padding-left: 32px;
  margin-top: 32px;
}
```

### Eyebrow Pill Badge
```css
.eyebrow-pill {
  display: inline-block;
  background-color: #FFE4C8;
  color: #F97A34;
  font-size: 26px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 14px 32px;
  border-radius: 99px;
  margin-bottom: 32px;
}
```

---

## 7. Slide Archetype Templates

Use one of these exact archetypes per slide. Do not invent new archetypes.

### Archetype A — BIG COVER SLIDE
- Background: `#FFFFFF` or `#1A1A2E`
- Eyebrow pill → "You should know this:" or topic label
- Giant headline (100–120px) in 2–3 lines
- 1 subheading line as body copy
- Slide counter: `01/05` top-right
- STRAUNT logo: bottom-right

### Archetype B — STAT SLIDE
- Background: `#F5F0EB` (cream)
- Eyebrow pill in orange
- Medium headline (72px) naming the problem
- Huge stat number (180px) in `--accent-orange`
- Stat label below in bold (36px)
- 2-line body copy with left indent bar
- STRAUNT logo: bottom-right

### Archetype C — LIST / INSIGHT SLIDE
- Background: `#FFFFFF`
- 3–4 line items, each with a small icon or number prefix
- Headline at top (72px)
- Items at 36px body text, 48px spacing between items
- Accent dots or numbers in orange

### Archetype D — QUOTE / ACCENT SLIDE
- Background: `#F97A34` (full orange) OR dark navy `#1A1A2E`
- Large pull-quote (80px) in `#FFFFFF`
- Attribution in small text below
- Large decorative quotation mark in background (opacity 15%)
- STRAUNT logo in white

### Archetype E — CTA CLOSURE SLIDE
- Background: `#1A1A2E` (dark navy)
- Headline: "Ready to Fix This?" or similar
- Sub-copy in white (36px)
- CTA button: `#F97A34` fill, white text, pill shape
- Social proof line: "700+ restaurants. 15–30% lift in orders."
- STRAUNT logo in white

---

## 8. Image Generation Rules (When AI Images Are Needed)

### When to Generate Images
Only generate AI imagery for:
1. **Cover slide feature photo** — a single, clean product or person photo on Option B style
2. **Decorative concept art** — used as a framed card inside the slide (not as full bleed)

### How to Prompt for AI Images
```
Generate a [subject description]. 
The image must have a CLEAN, MINIMAL background — either pure white or very soft light grey studio lighting.
NO textures, NO clutter, NO dark dramatic lighting.
The subject should be sharp and well-lit, as if shot by an editorial photographer.
Aspect ratio: 4:5 vertical.
Do NOT include any text or typography in the image.
Style reference: like the photography style in Sendify's marketing materials — clean, modern, professional.
```

### Overlay Requirement
If an AI image is used as SLIDE BACKGROUND (not framed card):
- **Always add** `background: linear-gradient(rgba(0,0,0,0), rgba(0,0,0,0.75))` overlay
- **Always verify** text contrast is WCAG AA compliant before shipping

---

## 9. CSS Boilerplate (Full Template)

Use this exact CSS skeleton for every `carousel.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #D1D5DB;
    display: flex;
    flex-direction: column;
    gap: 60px;
    align-items: center;
    padding: 60px 0;
    font-family: 'Plus Jakarta Sans', sans-serif;
  }

  .slide {
    width: 1080px;
    height: 1350px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 30px 60px rgba(0,0,0,0.20);
    background-color: #FFFFFF; /* Override per slide */
  }

  /* Overlay for photo-bg slides — apply inline if needed */
  .has-overlay::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(0,0,0,0) 10%, rgba(0,0,0,0.80) 100%);
    z-index: 1;
  }

  .safe-zone {
    position: absolute;
    inset: 0;
    padding: 108px 120px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    z-index: 2;
  }

  /* ── Utility: Top Row ── */
  .top-row {
    position: absolute;
    top: 72px;
    left: 120px;
    right: 120px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 3;
  }

  .slide-counter {
    font-size: 24px;
    font-weight: 600;
    color: #9CA3AF;
    letter-spacing: 1px;
  }

  /* ── Utility: Bottom Row ── */
  .bottom-row {
    position: absolute;
    bottom: 72px;
    left: 120px;
    right: 120px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    z-index: 3;
  }

  .logo {
    font-size: 26px;
    font-weight: 800;
    color: #111111;
    letter-spacing: 3px;
    text-transform: uppercase;
  }

  .logo.light { color: #FFFFFF; }

  /* ── Typography ── */
  .eyebrow-pill {
    display: inline-block;
    background-color: #FFE4C8;
    color: #F97A34;
    font-size: 26px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 14px 32px;
    border-radius: 99px;
    margin-bottom: 40px;
  }

  .eyebrow-pill.dark {
    background-color: rgba(249,122,52,0.2);
    color: #F97A34;
  }

  .headline {
    font-size: 100px;
    font-weight: 800;
    color: #111111;
    line-height: 1.0;
    letter-spacing: -4px;
    margin-bottom: 40px;
  }

  .headline-sm {
    font-size: 72px;
    font-weight: 800;
    color: #111111;
    line-height: 1.05;
    letter-spacing: -2px;
    margin-bottom: 36px;
  }

  .headline.light, .headline-sm.light { color: #FFFFFF; }

  .headline em, .headline-sm em {
    color: #F97A34;
    font-style: normal;
  }

  .accent-bar {
    width: 80px;
    height: 10px;
    background-color: #F97A34;
    border-radius: 5px;
    margin: 0 0 36px 0;
  }

  .body-copy {
    font-size: 36px;
    font-weight: 500;
    color: #4B5563;
    line-height: 1.65;
  }

  .body-copy.light { color: rgba(255,255,255,0.85); }

  .indent-bar {
    border-left: 10px solid #F97A34;
    padding-left: 32px;
    margin-top: 36px;
  }

  .stat-number {
    font-size: 180px;
    font-weight: 800;
    color: #F97A34;
    line-height: 1;
    letter-spacing: -6px;
    margin-bottom: 12px;
  }

  .stat-label {
    font-size: 36px;
    font-weight: 700;
    color: #111111;
    margin-bottom: 48px;
  }

  /* ── CTA Button ── */
  .cta-btn {
    display: inline-block;
    background-color: #F97A34;
    color: #FFFFFF;
    padding: 36px 72px;
    border-radius: 9999px;
    font-size: 40px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-top: 48px;
    box-shadow: 0 12px 32px rgba(249,122,52,0.35);
  }

  /* ── Decorative ── */
  .deco-circle {
    position: absolute;
    border-radius: 50%;
    background-color: #F5F0EB;
    z-index: 0;
  }

  .quote-mark {
    position: absolute;
    font-size: 600px;
    font-weight: 800;
    color: rgba(255,255,255,0.08);
    line-height: 1;
    top: -80px;
    left: -40px;
    z-index: 0;
    font-family: Georgia, serif;
  }
</style>
</head>
<body>
  <!-- Agent inserts <div class="slide"> blocks here -->
</body>
</html>
```

---

## 10. Quality Checklist — Before Exporting

Run through every slide and confirm:

- [ ] **Contrast:** Can you read every word at a glance? Is there enough contrast between text and bg?
- [ ] **Overlay:** If a photo is used as background, is the overlay applied? Is the text still readable?
- [ ] **Background type:** Is this a flat color or a minimal clean image? (NO busy textures)
- [ ] **Typography:** Is the headline the single dominant element? Is body copy short?
- [ ] **Eyebrow pill:** Is the label clearly visible with its pill background?  
- [ ] **Logo:** Is "STRAUNT" visible in the bottom-right corner?
- [ ] **Slide counter:** Is "01/05" style indicator showing?
- [ ] **Archetype match:** Does this slide use one of the 5 defined archetypes?
- [ ] **Reference match:** Could this slide plausibly sit alongside the reference images?

---

## 11. Anti-Patterns to Avoid Permanently

| ❌ Don't do this | ✅ Do this instead |
|---|---|
| Use busy AI-generated background textures | Use flat solid color `#FFFFFF`, `#F5F0EB`, `#1A1A2E` |
| Place dark text on a photographic BG without overlay | Add dark gradient overlay, switch text to white |
| Use Lexend for headlines (old font) | Use `Plus Jakarta Sans` |
| Add more than 2 text blocks to a slide | One headline + one body paragraph max |
| Mix 3+ colors on a single slide | Stick to BG color + text color + one accent |
| Use thin font weights for headlines | Headlines must be weight 800 always |
| Generate cluttered "dramatic" food/restaurant photos | Generate clean, minimal, studio-lit photos only |
| Skip the overlay on any full-bleed background image | Overlay is mandatory for all full-bleed images |
| Use the stat number and a long body copy in one slide | Either stat OR long copy — not both |
| Use padding: 216px (old default) | Use `padding: 108px 120px` for tighter, reference-accurate margins |
