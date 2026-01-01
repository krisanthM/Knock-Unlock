import json
import numpy as np
from extract_gaps import extract_time_gaps

with open("pattern.json") as f:
    data = json.load(f)

ref_mean = np.array(data["mean"])
ref_std = np.array(data["std"])

test = np.array(extract_time_gaps("knock.wav"))

def match(ref, std, test, k=2):
    if len(test) == 0 or test[0] == 0:
        return False

    if abs(len(ref) - len(test)) > 1:
        return False

    test = test[:len(ref)]

    ref_r = ref / ref[0]
    test_r = test / test[0]

    return np.all(np.abs(ref_r - test_r) <= k * (std / ref))

for attempt in range(2):
    if match(ref_mean, ref_std, test):
        print("✅ GRANTED")
        break
    else:
        print("Retry knock...")
else:
    print("❌ DENIED")
