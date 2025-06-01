import whisper
import pyttsx3
import speech_recognition as sr
import os

# Initialize TTS
tts = pyttsx3.init()
tts.say("NOVA is active and listening.")
tts.runAndWait()

# Record audio
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

# Save to file
with open("input.wav", "wb") as f:
    f.write(audio.get_wav_data())

# Load Whisper model
model = whisper.load_model("base")
result = model.transcribe("input.wav")
text = result["text"]

# Output
print("You said:", text)
tts.say(f"You said: {text}")
tts.runAndWait()
