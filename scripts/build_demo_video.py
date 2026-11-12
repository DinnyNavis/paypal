import os
import math
import wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import av

OUTPUT_VIDEO = r"D:\paypal-ai-main\paypal-ai-main\submission_assets\project_demo_3min.mp4"
BASE_FRAMES_DIR = r"D:\paypal-ai-main\paypal-ai-main\submission_assets\temp_video_bases"
AUDIO_DIR = r"D:\paypal-ai-main\paypal-ai-main\submission_assets\temp_audio"

FPS = 30
SAMPLE_RATE = 44100
TOTAL_DURATION = 177.0 # exactly 02:57
TOTAL_FRAMES = int(TOTAL_DURATION * FPS) # 5,310 frames
TOTAL_AUDIO_SAMPLES = int(TOTAL_DURATION * SAMPLE_RATE)

SEGMENT_DEFS = [
    {
        "id": "s01",
        "base": "v01_landing.png",
        "duration": 20.0,
        "title": "Problem & Instant Hook: Cross-Border 504 Timeouts",
        "takeaway": "Network timeouts cause catastrophic double-billing. PayBridge AI establishes truth.",
        "cursor_start": (960, 400),
        "cursor_end": (960, 680),
        "focal": (960, 540)
    },
    {
        "id": "s02",
        "base": "v02_invariants.png",
        "duration": 20.0,
        "title": "Architectural Invariants: AI Never Moves Money",
        "takeaway": "Autonomous agents produce analytical claims; only authenticated humans authorize mutations.",
        "cursor_start": (400, 350),
        "cursor_end": (960, 420),
        "focal": (960, 450)
    },
    {
        "id": "s03",
        "base": "v03_dashboard.png",
        "duration": 20.0,
        "title": "Executive Dashboard Matrix: 3D Financial State Vector",
        "takeaway": "Simultaneous observability across Gateway Truth, App State, and Bank Settlement.",
        "cursor_start": (300, 300),
        "cursor_end": (800, 480),
        "focal": (960, 480)
    },
    {
        "id": "s04",
        "base": "v04_demo.png",
        "duration": 20.0,
        "title": "Golden Path Demo B: PayPal Sandbox Order & 504 Timeout",
        "takeaway": "Simulated upstream drop triggers immediate DO_NOT_REPEAT_CHECKOUT session lock.",
        "cursor_start": (600, 400),
        "cursor_end": (1100, 520),
        "focal": (960, 500)
    },
    {
        "id": "s05",
        "base": "v05_timeline.png",
        "duration": 20.0,
        "title": "Autonomous Multi-Agent DAG: Agents A01–A10 Pipeline",
        "takeaway": "Gateway Ingestion reads Tier 1 PayPal capture data; Claim Validator screens raw payloads.",
        "cursor_start": (500, 350),
        "cursor_end": (950, 600),
        "focal": (960, 500)
    },
    {
        "id": "s06",
        "base": "v06_graph.png",
        "duration": 20.0,
        "title": "Interactive Truth Gap Graph: Pinpointing Asymmetry",
        "takeaway": "Visual consensus graph isolates GAP-01 (Lost Confirmation) for instant reassurance.",
        "cursor_start": (450, 400),
        "cursor_end": (1050, 480),
        "focal": (960, 480)
    },
    {
        "id": "s07",
        "base": "v07_dual_lens.png",
        "duration": 20.0,
        "title": "Two-Lens Symmetry: Coordinated Sender & Receiver Portals",
        "takeaway": "Buyer portal confirms captured funds while merchant portal tracks settlement.",
        "cursor_start": (400, 400),
        "cursor_end": (980, 540),
        "focal": (960, 520)
    },
    {
        "id": "s08",
        "base": "v08_passport.png",
        "duration": 20.0,
        "title": "Cryptographic Truth Passport: SHA-256 Consensus Seal",
        "takeaway": "Tamper-evident legal dossier citing immutable evidence references and public verification.",
        "cursor_start": (500, 350),
        "cursor_end": (1020, 560),
        "focal": (960, 540)
    },
    {
        "id": "s09",
        "base": "v09_ai_iris.png",
        "duration": 17.0,
        "title": "Aegis Iris AI Assistant: Sub-Second Financial Truth",
        "takeaway": "Private SLM conversational telemetry audit: one payment, two parties, one verified truth.",
        "cursor_start": (600, 600),
        "cursor_end": (1150, 720),
        "focal": (960, 540)
    },
]

print("Assembling master audio track (44,100 Hz, stereo)...")
master_audio = np.zeros((2, TOTAL_AUDIO_SAMPLES), dtype=np.int16)

current_time_offset = 0.0
for seg in SEGMENT_DEFS:
    seg_id = seg["id"]
    wav_path = os.path.join(AUDIO_DIR, f"{seg_id}.wav")
    if os.path.exists(wav_path):
        with wave.open(wav_path, "r") as wf:
            n_ch = wf.getnchannels()
            fr = wf.getframerate()
            n_frames = wf.getnframes()
            raw_bytes = wf.readframes(n_frames)
            
            samples = np.frombuffer(raw_bytes, dtype=np.int16)
            if n_ch == 2:
                samples = samples.reshape(-1, 2).T
            else:
                samples = np.array([samples, samples]) # mono to stereo
            
            # Resample if needed
            if fr != SAMPLE_RATE:
                new_len = int(samples.shape[1] * (SAMPLE_RATE / fr))
                resampled_0 = np.interp(
                    np.linspace(0, samples.shape[1], new_len),
                    np.arange(samples.shape[1]),
                    samples[0]
                ).astype(np.int16)
                resampled_1 = np.interp(
                    np.linspace(0, samples.shape[1], new_len),
                    np.arange(samples.shape[1]),
                    samples[1]
                ).astype(np.int16)
                samples = np.array([resampled_0, resampled_1])

            # Insert at offset + 0.6s
            start_idx = int((current_time_offset + 0.6) * SAMPLE_RATE)
            end_idx = min(start_idx + samples.shape[1], TOTAL_AUDIO_SAMPLES)
            actual_len = end_idx - start_idx
            if actual_len > 0:
                master_audio[:, start_idx:end_idx] = samples[:, :actual_len]
                print(f"Placed {seg_id} at {current_time_offset+0.6:.1f}s ({actual_len/SAMPLE_RATE:.2f}s)")
    current_time_offset += seg["duration"]

# Load base images
print("Loading base images...")
base_images = []
for seg in SEGMENT_DEFS:
    img_path = os.path.join(BASE_FRAMES_DIR, seg["base"])
    with Image.open(img_path) as im:
        base_images.append(im.convert("RGB").resize((1920, 1080), Image.Resampling.LANCZOS))

# Precompute mouse cursor asset
cursor_img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
c_draw = ImageDraw.Draw(cursor_img)
# Draw sleek pointer
cursor_pts = [(0, 0), (24, 18), (14, 18), (18, 28), (12, 30), (8, 20), (0, 24)]
c_draw.polygon(cursor_pts, fill=(255, 255, 255, 240), outline=(15, 23, 42, 255))

# Try default or truetype font
try:
    font_bold = ImageFont.truetype("arialbd.ttf", 26)
    font_sub = ImageFont.truetype("arial.ttf", 20)
    font_small = ImageFont.truetype("arial.ttf", 16)
except Exception:
    font_bold = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_small = ImageFont.load_default()

print("Opening PyAV container for H.264 / AAC export...")
os.makedirs(os.path.dirname(OUTPUT_VIDEO), exist_ok=True)
container = av.open(OUTPUT_VIDEO, mode="w")

vstream = container.add_stream("libx264", rate=FPS)
vstream.width = 1920
vstream.height = 1080
vstream.pix_fmt = "yuv420p"
vstream.options = {"crf": "20", "preset": "fast"}

astream = container.add_stream("aac", rate=SAMPLE_RATE)
astream.layout = "stereo"

print(f"Rendering {TOTAL_FRAMES} frames ({TOTAL_DURATION}s @ 30fps)...")

# Build frames
seg_frame_starts = []
accum = 0
for seg in SEGMENT_DEFS:
    seg_frame_starts.append(accum)
    accum += int(seg["duration"] * FPS)

audio_chunk_size = 1024
current_audio_sample = 0

for frame_idx in range(TOTAL_FRAMES):
    t = frame_idx / FPS
    
    # Determine active segment
    seg_idx = 0
    for i, s_start in enumerate(seg_frame_starts):
        if frame_idx >= s_start:
            seg_idx = i
        else:
            break
            
    seg = SEGMENT_DEFS[seg_idx]
    s_start_frame = seg_frame_starts[seg_idx]
    s_frames = int(seg["duration"] * FPS)
    progress_in_seg = (frame_idx - s_start_frame) / float(s_frames)
    
    # Base image with subtle zoom
    base_im = base_images[seg_idx]
    zoom = 1.0 + 0.025 * progress_in_seg
    if zoom > 1.001:
        zw = int(1920 / zoom)
        zh = int(1080 / zoom)
        fx, fy = seg["focal"]
        left = max(0, min(1920 - zw, int(fx - zw / 2)))
        top = max(0, min(1080 - zh, int(fy - zh / 2)))
        frame_im = base_im.crop((left, top, left + zw, top + zh)).resize((1920, 1080), Image.Resampling.BILINEAR)
    else:
        frame_im = base_im.copy()
        
    # Smooth crossfade for first 12 frames of segment
    if frame_idx > s_start_frame and (frame_idx - s_start_frame) < 12 and seg_idx > 0:
        prev_im = base_images[seg_idx - 1]
        alpha = (frame_idx - s_start_frame) / 12.0
        frame_im = Image.blend(prev_im, frame_im, alpha)
        
    # Animated cursor
    cx1, cy1 = seg["cursor_start"]
    cx2, cy2 = seg["cursor_end"]
    ease = 0.5 - 0.5 * math.cos(min(1.0, progress_in_seg * 1.5) * math.pi)
    cur_x = int(cx1 + (cx2 - cx1) * ease)
    cur_y = int(cy1 + (cy2 - cy1) * ease)
    
    # Draw click pulse at 40% progress
    draw = ImageDraw.Draw(frame_im, "RGBA")
    if 0.38 <= progress_in_seg <= 0.48:
        pulse_r = int((progress_in_seg - 0.38) * 100 * 25)
        pulse_alpha = int(max(0, 255 - (progress_in_seg - 0.38) * 2550))
        draw.ellipse(
            (cur_x - pulse_r, cur_y - pulse_r, cur_x + pulse_r, cur_y + pulse_r),
            outline=(6, 182, 212, pulse_alpha),
            width=3
        )
    
    # Composite cursor
    frame_im.paste(cursor_img, (cur_x, cur_y), cursor_img)
    
    # Draw lower-third broadcast banner (glassmorphic dark box)
    banner_box = (40, 940, 1880, 1055)
    draw.rounded_rectangle(banner_box, radius=16, fill=(10, 15, 30, 230), outline=(56, 189, 248, 120), width=2)
    
    # Status Pill
    pill_box = (60, 955, 350, 985)
    draw.rounded_rectangle(pill_box, radius=8, fill=(30, 41, 59, 240), outline=(99, 102, 241, 180), width=1)
    draw.text((72, 960), f"SEGMENT {seg_idx+1:02d}/09 | PAYBRIDGE AI", fill=(56, 189, 248), font=font_small)
    
    # Title & Takeaway
    draw.text((60, 992), seg["title"], fill=(241, 245, 249), font=font_bold)
    draw.text((60, 1024), seg["takeaway"], fill=(148, 163, 184), font=font_sub)
    
    # Timecode
    mins = int(t) // 60
    secs = int(t) % 60
    tc_str = f"{mins:02d}:{secs:02d} / 02:57"
    draw.text((1700, 960), tc_str, fill=(148, 163, 184), font=font_bold)
    
    # Progress Bar along very bottom
    bar_width = int(1840 * (frame_idx / float(TOTAL_FRAMES)))
    draw.rectangle((40, 1052, 40 + bar_width, 1055), fill=(6, 182, 212, 255))
    
    # Encode Video Frame
    vframe = av.VideoFrame.from_image(frame_im)
    vframe.pts = frame_idx
    for packet in vstream.encode(vframe):
        container.mux(packet)
        
    # Encode Audio chunk periodically to keep streams interleaved
    target_audio_sample = int(((frame_idx + 1) / float(TOTAL_FRAMES)) * TOTAL_AUDIO_SAMPLES)
    while current_audio_sample < target_audio_sample:
        chunk_len = min(audio_chunk_size, target_audio_sample - current_audio_sample)
        if chunk_len <= 0:
            break
        chunk = master_audio[:, current_audio_sample:current_audio_sample + chunk_len]
        aframe = av.AudioFrame.from_ndarray(chunk, format="s16p", layout="stereo")
        aframe.sample_rate = SAMPLE_RATE
        aframe.pts = current_audio_sample
        current_audio_sample += chunk_len
        for packet in astream.encode(aframe):
            container.mux(packet)
            
    if frame_idx % 300 == 0:
        print(f"Rendered {frame_idx}/{TOTAL_FRAMES} frames ({t:.1f}s / {TOTAL_DURATION}s)...")

# Flush remaining audio
while current_audio_sample < TOTAL_AUDIO_SAMPLES:
    chunk_len = min(audio_chunk_size, TOTAL_AUDIO_SAMPLES - current_audio_sample)
    chunk = master_audio[:, current_audio_sample:current_audio_sample + chunk_len]
    aframe = av.AudioFrame.from_ndarray(chunk, format="s16p", layout="stereo")
    aframe.sample_rate = SAMPLE_RATE
    aframe.pts = current_audio_sample
    current_audio_sample += chunk_len
    for packet in astream.encode(aframe):
        container.mux(packet)

# Flush encoders
print("Flushing stream encoders...")
for packet in vstream.encode():
    container.mux(packet)
for packet in astream.encode():
    container.mux(packet)

container.close()
print(f"Video export complete: {OUTPUT_VIDEO}")

