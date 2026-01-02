import json
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
from extract_gaps import extract_time_gaps

fs = 44100
seconds = 4
TARGET_SAMPLES = 5

patterns = []
expected_len = None

print("🔐 Enrollment started (5 valid samples required)")

while len(patterns) < TARGET_SAMPLES:
    input(f"\nPress ENTER and knock ({len(patterns)+1}/{TARGET_SAMPLES})")

    print("🎤 Recording...")
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    write("knock.wav", fs, audio)
    print("✅ Recorded")

    gaps = extract_time_gaps("knock.wav")
    print("Captured gaps:", gaps)

    if len(gaps) < 2:
        print("❌ Not enough knocks, retry")
        continue

    if expected_len is None:
        expected_len = len(gaps)
        print(f"🔒 Pattern length locked to {expected_len} gaps")

    if len(gaps) != expected_len:
        print(f"❌ Expected {expected_len} gaps, got {len(gaps)} — retry")
        continue

    # reject wildly inconsistent rhythms
    if max(gaps) / min(gaps) > 4:
        print("❌ Rhythm too inconsistent, retry")
        continue

    patterns.append(gaps)
    print("✅ Sample accepted")

patterns = np.array(patterns)

# MEDIAN IS SAFE NOW
mean_gaps = np.median(patterns, axis=0)
std_gaps = np.std(patterns, axis=0)

data = {
    "mean": mean_gaps.tolist(),
    "std": std_gaps.tolist()
}

with open("pattern.json", "w") as f:
    json.dump(data, f, indent=2)

print("\n✅ Enrollment completed successfully")
print("Mean gaps:", mean_gaps)
print("Std gaps :", std_gaps)
print("Pattern saved to pattern.json")
