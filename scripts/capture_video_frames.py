import os
import subprocess
from PIL import Image

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FRAMES_DIR = r"D:\paypal-ai-main\paypal-ai-main\submission_assets\temp_video_bases"
os.makedirs(FRAMES_DIR, exist_ok=True)

TARGETS = [
    ("v01_landing.png", "http://localhost:5173/?tab=landing"),
    ("v02_invariants.png", "http://localhost:5173/?tab=safe-action"),
    ("v03_dashboard.png", "http://localhost:5173/?tab=dashboard"),
    ("v04_demo.png", "http://localhost:5173/?tab=demo"),
    ("v05_timeline.png", "http://localhost:5173/?tab=timeline"),
    ("v06_graph.png", "http://localhost:5173/?tab=graph"),
    ("v07_dual_lens.png", "http://localhost:5173/?tab=sender-lens"),
    ("v08_passport.png", "http://localhost:5173/?tab=passport"),
    ("v09_ai_iris.png", "http://localhost:5173/ai-assistant.html"),
]

print("Capturing 1920x1080 base frames for demonstration video...")

for fname, url in TARGETS:
    out_path = os.path.join(FRAMES_DIR, fname)
    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--screenshot={out_path}",
        "--window-size=1920,1080",
        "--virtual-time-budget=4000",
        url
    ]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(out_path):
        with Image.open(out_path) as im:
            if im.size != (1920, 1080):
                im = im.resize((1920, 1080), Image.Resampling.LANCZOS)
            im.save(out_path, "PNG")
        print(f"Captured {fname} (1920x1080)")
    else:
        print(f"Failed {fname}")

print("Base frames capture complete.")

