import speech_recognition
import webbrowser

robot=speech_recognition.Recognizer()

you=""
with speech_recognition.Microphone() as mic:
    print("robot:I'm listening...")
    audio=robot.listen(mic)
    print("I'm listened")
    you=robot.recognize_google(audio)
test=False
you=you.lower()
if 'facebook' in you:
    test=True
elif 'youtube' in you:
    test=True
if test==False:
    webbrowser.open('https://www.google.com/search?q='+you)
elif test==True:
    webbrowser.open('https://www.'+you+'.com')    