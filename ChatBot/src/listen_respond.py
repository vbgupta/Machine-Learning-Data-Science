from dataclasses import dataclass
from playsound import  playsound
import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as mic:
        print("listening...")
        audio = recognizer.listen(mic)
    try:
        speech = recognizer.recognize_google(audio)
        print(speech)
    except:
        playsound("sounds/error_understand.mp3")

    return speech