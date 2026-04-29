---
name: generating-html-carousels
description: Technical workflow for generating pixel-perfect LinkedIn carousels using HTML/CSS. This skill must always be used together with carousel-visual-identity.md which governs all visual decisions.
depends_on: carousel-visual-identity.md
---

# Hybrid HTML Carousel Generation Protocol

## STEP 0 — MANDATORY: Read the Visual Identity Skill First

> Before writing a single line of HTML or generating a single image, you MUST read and internalize:  
> **`.agents/skills/design/carousel-visual-identity.md`**
>
> Every visual decision — backgrounds, typography, colors, layout, overlays — is governed by that skill.  
> This file only covers the mechanical workflow. Do NOT make visual decisions from this file alone.

---

## When to use this skill
- You have finalized the textual content and the visual concept for a LinkedIn post.
- You are ready to generate and assemble the final slide graphics.
- **DO NOT USE STITCH MCP** for this process.

---

## The Workflow

### Phase 1 — Decide Background Strategy Per Slide

For each slide, consult `carousel-visual-identity.md` Section 5 (Background Strategy) and classify:

| Slide | Background Type | Action |
|---|---|---|
| A: Text-only slides | Flat solid color | No image needed — use CSS only |
| B: Cover with framed photo | Flat BG + photo card | Generate photo with clean studio BG |
| C: Full-bleed photo | Photo + mandatory overlay | Generate photo AND add overlay div |

**Default for 80% of slides: Flat solid color. Do not generate AI images unless explicitly needed.**

---

### Phase 2 — Generate Background Assets (Only When Needed)

Only generate AI images for slides classified as type B or C above.

#### Tool Instructions
1. Use the `generate_image` tool.
2. In the `ImagePaths` parameter, **include 1–2 reference images** from `Image references/` folder.
3. Use this prompt template:
```
Generate a [subject]. 
Clean minimal background — pure white or soft light grey studio lighting.
NO busy textures, NO dramatic lighting, NO clutter.
Subject is sharp and editorial, like professional marketing photography.
4:5 vertical aspect ratio.
Do NOT include any text or words in the image.
Reference style: clean, modern product/editorial photography.
```
4. Name outputs: `slide_1_bg`, `slide_2_bg`, etc.
5. For any full-bleed use: add the `.has-overlay` class and CSS overlay from the identity skill.

---

### Phase 3 — Write `carousel.html`

Use ONLY the CSS boilerplate from `carousel-visual-identity.md` Section 9.

#### Layout Rules (1080×1350px Canvas)
- Each `.slide` must be exactly `width: 1080px; height: 1350px`
- Use `.safe-zone` with `padding: 108px 120px` — NOT the old 216px
- Use `Plus Jakarta Sans` font — NOT Lexend
- Apply archetype templates from the identity skill Section 7

#### Overlay Application (MANDATORY for photo backgrounds)
```html
<!-- For any slide with a photo background, ALWAYS add this structure: -->
<div class="slide has-overlay" style="background-image: url('slide_1_bg.png')">
  <!-- has-overlay triggers the ::after dark gradient overlay -->
  <!-- All text inside safe-zone must use class="light" -->
  <div class="safe-zone">
    <h1 class="headline light">Your Headline</h1>
    <p class="body-copy light">Supporting copy.</p>
  </div>
  <div class="bottom-row">
    <span class="logo light">STRAUNT</span>
  </div>
</div>
```

#### Per-Slide Background Overrides
```html
<!-- Option A: Flat white -->
<div class="slide" style="background-color: #FFFFFF;">

<!-- Option A: Flat cream -->
<div class="slide" style="background-color: #F5F0EB;">

<!-- Option A: Dark navy -->
<div class="slide" style="background-color: #1A1A2E;">

<!-- Option A: Full orange (accent slide) -->
<div class="slide" style="background-color: #F97A34;">

<!-- Option C: Photo with overlay (RARE — add has-overlay class) -->
<div class="slide has-overlay" style="background-image: url('slide_X_bg.png');">
```

---

### Phase 4 — Export to PNG

Once `carousel.html` is saved:

```bash
node export_carousel.js
```

This generates `slide_1.png`, `slide_2.png`, etc. in the workspace root.

---

## Pre-Export Quality Gate

Before running the export script, verify every slide passes the checklist in `carousel-visual-identity.md` Section 10.

If any slide fails, fix the HTML before exporting — do not ship broken slides.
