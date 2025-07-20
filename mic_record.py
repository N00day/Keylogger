import sounddevice as sd
from scipy.io.wavfile import write

def record_mic(duration=10):
  fs = 44100
  recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
  sd.wait()
  write("logs/audio.wav", fs, recording)