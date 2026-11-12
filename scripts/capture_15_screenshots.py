import os
import subprocess
import time
from PIL import Image

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
OUTPUT_DIR = r"D:\paypal-ai-main\paypal-ai-main\submission_assets\image_gallery_15"
os.makedirs(OUTPUT_DIR, exist_ok=True)

TARGETS = [
    ("01_landing_showcase.png", "http://localhost:5173/?tab=landing", "Landing Showcase & Cross-Border Problem Statement"),
    ("02_enterprise_dashboard.png", "http://localhost:5173/?tab=dashboard", "3D Executive Financial Truth Matrix & Telemetry"),
    ("03_rbac_security_auth.png", "http://localhost:5173/?tab=auth", "Role-Based Access Control & Cryptographic Key Management"),
    ("04_paypal_checkout_gateway.png", "http://localhost:5173/?tab=new-payment", "Cross-Border PayPal Checkout Initiation"),
    ("05_safe_action_lock_guard.png", "http://localhost:5173/?tab=safe-action", "Deterministic Safe-Action Lock & Mutation Guard"),
    ("06_golden_path_interactive_stepper.png", "http://localhost:5173/?tab=demo", "Interactive 7-Stage Golden Path Demonstration Engine"),
    ("07_case_investigation_detail.png", "http://localhost:5173/?tab=cases&case=c101-demo-4567-89ab-cdef00000001", "Case Investigation Detail & AI Diagnostic Claims"),
    ("08_truth_gap_graph_visualizer.png", "http://localhost:5173/?tab=graph", "Cross-Entity Truth Gap Graph Visualizer"),
    ("09_lifecycle_timeline_vector.png", "http://localhost:5173/?tab=timeline", "Multi-Rail Financial Lifecycle Timeline Vector"),
    ("10_sender_two_lens_view.png", "http://localhost:5173/?tab=sender-lens", "Sender Two-Lens Financial Perspective"),
    ("11_receiver_two_lens_view.png", "http://localhost:5173/?tab=receiver-lens", "Receiver Two-Lens Financial Perspective & Payout Lock"),
    ("12_cryptographic_truth_passport.png", "http://localhost:5173/?tab=passport", "Cryptographic Truth Passport & SHA-256 Audit Anchor"),
    ("13_recovery_mirror_consensus.png", "http://localhost:5173/?tab=mirror", "Recovery Mirror Bilateral Consensus & Settlement"),
    ("14_operations_double_entry_ledger.png", "http://localhost:5173/?tab=operations", "Double-Entry Ledger & Real-Time Webhook Engine"),
    ("15_ai_financial_copilot_iris.png", "http://localhost:5173/ai-assistant.html", "Iris AI Autonomous Financial Copilot & Agent Swarm")
]

print(f"==================================================")
print(f"Capturing exactly {len(TARGETS)} unique screenshots...")
print(f"Destination: {OUTPUT_DIR}")
print(f"==================================================")

success_count = 0

for idx, (filename, url, description) in enumerate(TARGETS, 1):
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
    print(f"[{idx:02d}/15] Capturing: {filename}")
    print(f"       Description: {description}")
    print(f"       URL: {url}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    
    if os.path.exists(dest_path):
        with Image.open(dest_path) as im:
            # Enforce exact 1800x1200 (3:2) resolution and optimize
            if im.size != (1800, 1200):
                im = im.resize((1800, 1200), Image.Resampling.LANCZOS)
            im.save(dest_path, "PNG", optimize=True)
        size = os.path.getsize(dest_path)
        print(f"       Status: SUCCESS ({size:,} bytes, {size/1024/1024:.2f} MB)")
        success_count += 1
    else:
        print(f"       Status: FAILED (file not created)")

print(f"==================================================")
print(f"Completed: {success_count}/{len(TARGETS)} screenshots captured successfully.")
print(f"==================================================")
