import sounddevice as sd
import soundfile as sf

def record_audio(filename="input.wav", duration=4, samplerate=22050):
    print("🎤 Speak now...")
    # Start recording
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    # Wait for it to finish recording
    sd.wait()
    # Save as WAV file
    sf.write(filename, audio, samplerate)
    print(f"✅ Audio saved as {filename}")
