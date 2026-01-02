import librosa
import numpy as np

MIN_GAP = 0.18          # seconds (180 ms)
SMOOTH_WINDOW = 200     # samples
ENERGY_FACTOR = 3.5    # adaptive threshold multiplier

def extract_time_gaps(file):
    # Load audio
    y, sr = librosa.load(file, sr=None)

    # Convert to energy envelope
    energy = np.abs(y)

    # Smooth energy (moving average)
    energy_smooth = np.convolve(
        energy,
        np.ones(SMOOTH_WINDOW) / SMOOTH_WINDOW,
        mode="same"
    )

    # Adaptive threshold
    threshold = ENERGY_FACTOR * np.mean(energy_smooth)

    # Peak detection
    peaks = np.where(energy_smooth > threshold)[0]

    knock_times = []
    last_knock = -sr

    for p in peaks:
        # Enforce minimum gap
        if p - last_knock > MIN_GAP * sr:
            # Enforce minimum knock strength
            if energy_smooth[p] > threshold:
                knock_times.append(p / sr)
                last_knock = p

    # Need at least 2 knocks
    if len(knock_times) < 2:
        return []

    gaps = np.diff(knock_times)
    return gaps.tolist()


if __name__ == "__main__":
    print(extract_time_gaps("knock.wav"))
