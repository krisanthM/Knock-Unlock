import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 4

print("Knock now...")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

write("knock.wav", fs, audio)
print("Saved knock.wav")
