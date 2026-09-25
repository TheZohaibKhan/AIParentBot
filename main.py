from record_audio import record_audio
from emotion_detector import predict_emotion
from text_to_speech import speak
from memory_database import init_memory as init_db, save_conversation
from speech_to_text import transcribe_audio
from chatgpt_response import get_chatgpt_response

def main():
    init_db()  # Initialize the SQLite memory database
    
    print("🎤 Speak now...")
    record_audio("input.wav")  # Record audio and save as 'input.wav'
    print("✅ Audio saved as input.wav")
    
    emotion = predict_emotion("input.wav")  # Predict emotion from voice
    print(f"🎭 Detected Emotion: {emotion}")
    
    user_input = speech_to_text("input.wav")  # Transcribe audio to text
    print(f"🗣️ Transcribed: {user_input}")
    
    bot_reply = get_chatgpt_response(user_input, emotion)  # Get ChatGPT's reply
    print("🤖 Bot says:", bot_reply)
    
    speak(bot_reply)  # Convert response to speech
    
    save_conversation(user_input, emotion, bot_reply)  # Save conversation to DB

if __name__ == "__main__":
    main()
