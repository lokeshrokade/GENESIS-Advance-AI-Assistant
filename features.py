from pygame import mixer
from pyttsx3 import Engine
import speech_recognition as sr
import pyttsx3
import pygame
from time import sleep
from win10toast import ToastNotifier
import datetime

listener = sr.Recognizer()
engine: Engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
selected_voice = None
for v in voices:
    try:
        if 'female' in (v.name or '').lower():
            selected_voice = v
            break
    except Exception:
        continue
if selected_voice is None and voices:
    selected_voice = voices[min(0, len(voices) - 1)]
if selected_voice is not None:
    engine.setProperty('voice', selected_voice.id)
engine.setProperty('rate', 171)
engine.setProperty('volume', 150)
pygame.init()
try:
    mixer.music.load("C://Users//idmak//Music//intro0.mp3")
    mixer.music.play()
    mixer.music.set_volume(50)
except Exception:
    pass
reminders = "Nothing"



def sounds():
    try:
        mixer.music.load("C://Users//idmak//Music//intro2.mp3")
        mixer.music.play()
        mixer.music.set_volume(0.2)
    except Exception:
        pass

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said : {query}")

    except:
        return ""

    query = str(query)
    return query.lower()

def notification(title, desc):
    toaster = ToastNotifier()
    toaster.show_toast(title, desc, duration=5, threaded=True)
def intro():

    sounds()
    ampm = datetime.datetime.now().strftime('%p')
    hour = datetime.datetime.now().strftime('%I')
    hour = int(hour)
    if "AM" in ampm:
        talk("hello sir, good morning")
    elif "PM" in ampm and hour < 4:
        talk("hello sir, good afternoon ")
    elif "PM" in ampm and hour > 3:
        talk("hello sir, good evening")
    else:
        talk("good night")

    time = datetime.datetime.now().strftime('%I:%M %p')
    notification("Time", 'Current time is ' + time)
    talk('Current time is ' + time)

    talk("how can i help you sir")
