import json
import numpy as np
import os
import time
from extract_gaps import extract_time_gaps

# safety: ensure fresh audio
age = time.time() - os.path.getmtime("knock.wav")
if age > 5:
    print("❌ Old recording, record again")
    exit()

with open("pattern.json") as f:
    data = json.load(f)

ref = np.array(data["mean"])

def ratio_only_match(ref, test, tol=0.25):
    """
    Ratio-only matcher (MOST STABLE)
    tol = 0.25 → allows ~25% timing variation
    """

    ref = np.array(ref)
    test = np.array(test)

    if len(test) != len(ref):
        return False

    if ref[0] == 0 or test[0] == 0:
        return False

    # ratio normalization
    ref_r = ref / ref[0]
    test_r = test / test[0]

    return np.all(np.abs(ref_r - test_r) <= tol)


for attempt in range(2):

    if attempt > 0:
        print("🎤 Re-recording...")
        os.system("python record_knock.py")

    test = np.array(extract_time_gaps("knock.wav"))
    print("Test gaps:", test.tolist())

    if ratio_only_match(ref, test):
        print("✅ GRANTED")
        break
    else:
        print("Retry knock...")

else:
    print("❌ DENIED")
