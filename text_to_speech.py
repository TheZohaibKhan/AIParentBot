from elevenlabs.client import ElevenLabs
from elevenlabs import play, save
# Set your API key
api_key = "sk_c02db658c6408ff757c10ccca7c80527898011afa0b94d67"  # Replace with your actual API key
client = ElevenLabs(api_key=api_key)

def speak(text, voice="Rachel", output_path="output.wav"):
    audio = client.generate(
        text=text,
        voice=voice,
        model="eleven_multilingual_v2"
    )
    save(audio, output_path)
    play(audio)
