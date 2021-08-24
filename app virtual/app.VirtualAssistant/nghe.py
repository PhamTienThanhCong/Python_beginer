import os
import pyaudio
import speech_recognition
import pyttsx3
from googlesearch import search

robot=speech_recognition.Recognizer()

def noi(say):
    engine = pyttsx3.init()
    print("robot: "+say)
    engine.say(say)
    engine.runAndWait()

while True:
    you=""
    with speech_recognition.Microphone() as mic:
        print("robot:I'm listening...")
        audio=robot.listen(mic)
        print("I'm listened")
        you=robot.recognize_google(audio)
    print(you)
    
    # if you=="":
    #     noi("i don't known")
    # elif "hello" in you:
    #     noi("hello, cong")
    # elif "bye" in you:
    #     noi("good bye, cong")
    #     break
    # elif "your name" in you:
    #     noi("my name is Alex")
    # elif "turn off my computer" in you:
    #     os.system("shutdown /p")