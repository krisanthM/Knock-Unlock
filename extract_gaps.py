import librosa
import numpy as np

def extract_time_gaps(file, threshold=0.02):
    y, sr = librosa.load(file, sr=None)
    energy = np.abs(y)

    # simple peak detection
    peaks = np.where(energy > threshold)[0]

    # group peaks into knocks
    knock_times = []
    last = -sr
    for p in peaks:
        if p - last > 0.18 * sr:  # 180 ms
            knock_times.append(p / sr)
            last = p

    # compute time gaps
    gaps = np.diff(knock_times)
    return gaps.tolist()

if __name__ == "__main__":
    print(extract_time_gaps("knock.wav"))
