import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 3

print("🎤 Recording for", seconds, "seconds... Knock now!")

audio = sd.rec(
    int(seconds * fs),
    samplerate=fs,
    channels=1,
    dtype="int16"
)

sd.wait()  # waits until recording is DONE

write("knock.wav", fs, audio)

print("✅ Recording finished. Saved as knock.wav")
