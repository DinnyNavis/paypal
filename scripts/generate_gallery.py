import os
import subprocess
import time
from PIL import Image

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
OUTPUT_DIR = r"D:\paypal-ai-main\paypal-ai-main\submission_assets\image_gallery"
os.makedirs(OUTPUT_DIR, exist_ok=True)

TARGETS = [
    ("01_hero_distill_scanner.png", "http://localhost:5173/?tab=landing"),
    ("02_enterprise_dashboard.png", "http://localhost:5173/?tab=dashboard"),
    ("03_golden_path_demo_stepper.png", "http://localhost:5173/?tab=demo"),
    ("04_timeout_safe_action_lock.png", "http://localhost:5173/?tab=safe-action"),
    ("05_truth_gap_graph_analysis.png", "http://localhost:5173/?tab=graph"),
    ("06_lifecycle_timeline_vector.png", "http://localhost:5173/?tab=timeline"),
    ("07_case_detail_sender_lens.png", "http://localhost:5173/?tab=sender-lens"),
    ("08_case_detail_receiver_lens.png", "http://localhost:5173/?tab=receiver-lens"),
    ("09_cryptographic_truth_passport.png", "http://localhost:5173/?tab=passport"),
    ("10_recovery_mirror_resolution.png", "http://localhost:5173/?tab=mirror"),
    ("11_ai_financial_assistant_iris.png", "http://localhost:5173/ai-assistant.html"),
    ("12_operations_double_entry_ledger.png", "http://localhost:5173/?tab=operations"),
]

print(f"Starting capture of {len(TARGETS)} screenshots at 1800x1200 (3:2 ratio)...")

for filename, url in TARGETS:
    dest_path = os.path.join(OUTPUT_DIR, filename)
    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--screenshot={dest_path}",
        "--window-size=1800,1200",
        "--virtual-time-budget=4000",
        url
    ]
    print(f"Capturing: {filename} from {url}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(dest_path):
        size = os.path.getsize(dest_path)
        with Image.open(dest_path) as im:
            dims = im.size
            # Ensure exact dimensions and optimize
            if dims != (1800, 1200):
                im = im.resize((1800, 1200), Image.Resampling.LANCZOS)
            im.save(dest_path, "PNG", optimize=True)
            size = os.path.getsize(dest_path)
        print(f" -> SUCCESS: {filename} | Dims: 1800x1200 | Size: {size:,} bytes (<5MB: {size < 5000000})")
    else:
        print(f" -> FAILED to capture {filename}")

print("\nGallery capture process finished.")

