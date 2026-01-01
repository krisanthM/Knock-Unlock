import json
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
from extract_gaps import extract_time_gaps

fs = 44100
seconds = 4

patterns = []
expected_len = None
TARGET_SAMPLES = 5

print("🔐 Enrollment started (5 valid samples required)")

while len(patterns) < TARGET_SAMPLES:
    idx = len(patterns) + 1
    input(f"\nPress ENTER and knock ({idx}/{TARGET_SAMPLES})")

    print("🎤 Recording...")
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    write("knock.wav", fs, audio)
    print("✅ Recorded")

    gaps = extract_time_gaps("knock.wav")
    print("Captured gaps:", gaps)

    # basic validity check
    if len(gaps) < 1:
        print("⚠️ No valid knock detected, retry this sample")
        continue

    # lock pattern length from first valid sample
    if expected_len is None:
        expected_len = len(gaps)
        print(f"✅ Pattern length locked to {expected_len} gaps")

    # reject inconsistent samples
    if len(gaps) != expected_len:
        print(f"❌ Expected {expected_len} gaps, got {len(gaps)} — retry")
        continue

    patterns.append(gaps)
    print("✅ Sample accepted")

patterns = np.array(patterns)

mean_gaps = patterns.mean(axis=0)
std_gaps = patterns.std(axis=0)

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
