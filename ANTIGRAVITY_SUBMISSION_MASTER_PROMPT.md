# ANTIGRAVITY — FINAL HACKATHON SUBMISSION ASSET PRODUCTION

**Role:** Act as a senior product-demo director, QA engineer, browser-automation specialist, video editor, and hackathon pitch coach. This is a **production task** on the **existing project already in this workspace**. Do not scaffold a new project, redesign the app, or substitute mockups for real UI.

## Goal

Produce **two judge-ready submission assets** directly from the finished, working application:

1. **Image gallery:** up to 15 authentic screenshots, PNG or JPG, each **under 5 MB**, ideally **3:2**, professionally framed and legible.
2. **Demonstration video:** **one real, high-quality screen-recorded MP4**, **under 3 minutes** (target **02:56–02:58**, absolute maximum 02:59), with the most important value and working flow shown inside the first three minutes. Target **1920 × 1080, 30 fps, H.264 video / AAC audio**.

Additionally, create a **separate, project-specific `PITCH_SCRIPT_20_SECOND_SEGMENTS.md`** file with **nine sections**, one for each 20-second window from `00:00` to `03:00`. The script must match the video, sound natural in spoken English, and use verified project facts only.

**Critical clarification:** A real application screenshot does **not** mean a screenshot of the Antigravity workspace, project folder, VS Code, terminal, file explorer, README, code, or a static pitch slide. Capture the **running end-user website/app only**. Likewise, the video must show a **real product walkthrough**, not folders, code, simulated product UI, or slide-only screens. You may store deliverables in a folder; do not *record or screenshot the folder itself*.

## 1. Inspect and understand the EXISTING project first

- Examine the repository structure, README, package manifests, configuration templates, routes, API, frontend, backend, database/data dependencies, tests, and the actual user journey.
- Identify the real project name, one-line value proposition, target user, specific problem, 3–5 strongest verified product features, real AI capabilities (if any), payment/PayPal integration (if any), and the actual final user outcome.
- Run or connect to the EXISTING application using its normal setup. Verify backend/API and frontend health. Use only safe demo/test data. If it is already hosted, use the actual hosted experience when appropriate.
- For a PayPal-enabled project, show a genuine **sandbox** payment/checkout/event/verification flow *only if implemented and safe to demonstrate*. Never pretend a production transaction happened. Never reveal PayPal credentials, tokens, private account details, API keys, or private customer information.
- Verify the key feature path by clicking through it. Record what actually works. Do not invent features, metrics, logos, testimonials, users, transactions, or results.
- If something breaks, make minimal safe fixes required to demonstrate the existing product and verify again; do not change core business behavior or falsify output. Note any unresolved limitation in the final report.

## 2. Select the most compelling demonstration journey

Construct one cohesive story: **problem → product → main workflow → differentiating capability → verifiable outcome → closing value**.

Choose the order based on the real repo, not on this example. Prioritize the biggest visual proof of value within the opening **20–40 seconds**. Do not spend the first minute on a logo or a generic introductory slide.

Suggested gallery storyboard (choose only screens that exist; do **not** manufacture missing pages):

1. Product hero or initial dashboard showing what the app does.
2. Clear entry point / key action.
3. Main workflow — first meaningful user input.
4. Main workflow — processing or intelligent step where visually useful.
5. Most differentiated or AI-assisted feature (if implemented).
6. Real result, actionable recommendation, or generated outcome.
7. Secondary feature showing breadth without repetition.
8. Transaction/PayPal sandbox integration screen, if implemented.
9. Confirmation, tracking, history, or audit view, if implemented.
10. Final high-impact output / completed journey.

**Do not force ten images**: 6–10 excellent authentic screenshots are better than 15 repetitive ones; maximum 15.

## 3. Gallery capture specifications

- Use Playwright, browser automation, or the available browser tool to navigate the **live running app** at a consistent desktop viewport. Wait for fonts, images, data, and animations to settle; disable distracting overlays, debug UI, notification pop-ups, browser chrome, and devtools.
- Prefer screenshots at **1800 × 1200** (exact **3:2**) or **1920 × 1280**, then export optimized PNG/JPG preserving legible text and crisp details. Do not distort the page to force aspect ratio; crop thoughtfully or add neutral matching canvas padding only if needed.
- Every gallery image must be **< 5,000,000 bytes**, and preferably comfortably below the limit. No GIF unless animation contributes significant evidence; for GIF also obey the 5 MB limit.
- Frame one important feature per screenshot; keep headings, key inputs, buttons, and result visible. Capture natural, genuine demo states. Avoid duplicate screenshots, half-loaded spinners, blank/error screens, tiny text, login credentials, and personal data.
- Use filenames `01_hero.png`, `02_key_action.png`, etc., with accurate filenames based on real screens. Store in `submission_assets/image_gallery/`.
- Create `submission_assets/IMAGE_GALLERY_CAPTIONS.md` with one short, factual, judge-friendly caption per image, in the exact submission order.
- Check all outputs for dimensions, legibility, duplicates, compression, private data, and file size.

## 4. Produce a real, polished 3-minute video

**Video must come from direct recording of the actual app** (screen capture/browser automation). Use a reliable native screen recorder, Playwright browser/video recording, OBS, or an equivalent tool that is available and working in this environment. Use FFmpeg for trim/crop/scale/composition/encoding if available.

- Format: `submission_assets/project_demo_3min.mp4`.
- Target length: **2:56–2:58**; hard limit: **under 3:00**, verify with `ffprobe` or equivalent.
- Format: **1920×1080 (16:9), 30 fps, MP4, H.264, yuv420p**, AAC audio if narration exists. Capture at high enough resolution to keep small UI labels readable; zoom the app/capture area intelligently when needed.
- Start with the working product and value proposition immediately. Spend a maximum of 3 seconds on an opening title if it truly helps; judges should see actual product action right away.
- Create **one cohesive walkthrough**, with cursor movements and clicks performed purposefully; show input → action → response → result. Smoothly cut waiting, loading, browser navigation, typos, and dead time without changing the real result.
- Avoid shakiness, scroll spam, visually distracting mouse movement, excess animation, low-quality AI-generated replacement screens, unrelated stock footage, long intro/outro, IDE/folder/terminal shots, and raw debug logs.
- Use restrained, readable on-screen captions for the core value proposition and key moments. Captions must not cover important UI.
- Narration: Prefer a clear **natural spoken-English voiceover** recorded by the presenter if available. If authorized TTS tools are present, a clear natural TTS track may be used, but do not invent a recording or claim narration exists if it does not. **Never delay or replace the actual video because TTS is unavailable**; produce a readable product video with concise captions and export a matching narration script for later voice recording.
- No copyrighted music unless appropriately licensed. Either skip background music or ensure speech remains intelligible.
- Remove/mask secrets and private data. Use sandbox or safe test accounts. Do not upload the video publicly or log into YouTube without explicit user permission.

### Strict 20-second timing map

The final voiceover should track nine 20-second **editorial sections** (the final closing section can be shortened slightly in the cut so the export stays under 3:00):

| Segment | Video range | What the judges must understand |
|---|---|---|
| 1 | 00:00–00:20 | The problem, intended user, instant product hook |
| 2 | 00:20–00:40 | What the app is and why the solution is different |
| 3 | 00:40–01:00 | First interaction / actual input |
| 4 | 01:00–01:20 | Core feature in action |
| 5 | 01:20–01:40 | Most important AI/automation/decision capability, if real |
| 6 | 01:40–02:00 | Real produced result and user benefit |
| 7 | 02:00–02:20 | Second proof point or integration (PayPal sandbox if implemented) |
| 8 | 02:20–02:40 | End-to-end completion, reliability/privacy/technical quality evidenced in app |
| 9 | 02:40–02:58 | Impact, differentiator, compelling close |

Aim for **35–43 naturally spoken words per 20-second section**. Keep each section focused on what is actually visible in that section. Say the exact project/product name correctly.

## 5. Write the project-specific pitch MD, not a generic template

Create `submission_assets/PITCH_SCRIPT_20_SECOND_SEGMENTS.md` containing:

- **Project title** (verified from repo).
- **One-sentence summary** grounded in actual implementation.
- **Nine clearly labeled 20-second script sections** with timecode, exact spoken-English narration, on-screen action, caption/visual cue, and intended key takeaway.
- Spoken content must be **clear, confident, natural, simple English**; no hype, fabricated claims, or hard-to-pronounce jargon. Explain the problem, product, differentiator, real feature demonstration, outcome, and impact.
- If the project actually integrates PayPal, accurately describe the supported payment flow and label demo transactions as **sandbox**; otherwise, do not imply PayPal integration.
- **Recording notes** for pronunciation, pacing, screen transitions, and avoiding sensitive information.
- **YouTube title, 2–3 sentence description**, and recommended thumbnail frame (without uploading).
- **One checklist** verifying each script sentence matches a real on-screen action.

## 6. Quality-control / acceptance tests (mandatory)

Before completion, inspect files and verify:

- `image_gallery` contains 1–15 distinct real screenshots, ideally 6–10; each PNG/JPG/GIF under 5 MB; every one is 3:2 or carefully framed to submission specification.
- The images show **actual project UI**, not code, editor, Explorer/folder, browser errors, slides, or artificial mockups.
- The video file **exists, opens, plays all the way through**, is clear at 1080p, has no black/frozen sections, and has runtime **<180 seconds**. If audio is present, verify it is audible and synchronized.
- The main feature and actual result are visible in the demo, rather than only described.
- `PITCH_SCRIPT_20_SECOND_SEGMENTS.md` contains **all nine 20-second sections**, matching recorded timestamps and the real app.
- Secrets/credentials/private data are not visible; no invented product functions, metrics, or outcomes.
- If a browser or recording capability is missing, **do not falsely report success or create a slideshow and call it a screen-recorded demo**. Try the available real capture alternatives; report the exact unresolved blocker and leave verified assets intact.

## 7. Final handoff, in one place

Deliver this structure, using relative repo paths:

```text
submission_assets/
├── image_gallery/
│   ├── 01_<actual_screen>.png
│   ├── 02_<actual_screen>.png
│   └── ...
├── project_demo_3min.mp4
├── PITCH_SCRIPT_20_SECOND_SEGMENTS.md
├── IMAGE_GALLERY_CAPTIONS.md
└── SUBMISSION_QA_REPORT.md
```

The QA report must list actual screenshot filenames, dimensions and byte sizes; verified video resolution, frame rate, duration and playback check; a short description of the demonstrated app flow; any issues and fixes; and any remaining manual steps. Do not claim tools or media were created unless the files exist and have been verified.

**Important final submission note:** YouTube is the **only accepted video platform**. The user must upload `project_demo_3min.mp4` to YouTube and set visibility to **Public** or **Unlisted**, with **no password**, then paste the URL into the submission form. Do not claim the local MP4 is itself the YouTube link. The image gallery must be uploaded individually in the site's supported JPG/PNG/GIF format.

**Execute this task now against this existing workspace. Do not stop after giving advice, a plan, a template, or a prompt. Produce and validate the actual asset files to the extent supported by the environment.**
