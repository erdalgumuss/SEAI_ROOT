# src/services/text/transcription.py

import speech_recognition as sr

class TranscriptionService:
    def transcribe_audio(self, audio_path):
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
        return text
