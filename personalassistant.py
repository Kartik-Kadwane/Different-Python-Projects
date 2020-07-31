import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak("Welcome back")
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    #print(Time)
    speak(f"The Current Time is {Time}")

#speak("Welcome back")
time()

def wiki():
    query="Iphone"
    result=wikipedia.summary(query,sentences=3)
    speak("According to wikipedia")
    print(result)
    speak(result)
#wiki()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        print("1***************")
        r.pause_threshold = 1
        print("2***************")
        audio = r.listen(source)
        print("3***************")
    
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-ln')
        print(f"You said :{query}\n")
    
    except Exception as e:
        print(e)
        print("Say that Again....")
        speak("Say that Again....")
        return "None"
    return query
  
takecommand()