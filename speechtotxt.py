import pyttsx3 
import speech_recognition as sr
def get():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Om")
        audio = r.listen(source)
        print("done")

    try:
        text = r.recognize_google(audio)
        print("you said :::"+text)
    except Exception as e:
        print(e)


get()
