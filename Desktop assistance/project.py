import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit

chrome="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Priyam sir, I am your assistant. Please tell how may I help you")

def take():
    #take input from user from microphone and returns string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1     #time in sec before it thinks that sentence is completed
        audio=r.listen(source)  #listening

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')    #google will recognize it
        print("You said: ",query)

    except Exception:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query=take().lower()

        # Now according to query we will perform operations
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query=query.replace("wikipedia","")    #removing thw word wikipedia from sentence
            results=wikipedia.summary(query, sentences=2)   #2 sentences from wiki will be given
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.get(chrome).open("youtube.com")
        elif 'listen' in query:
            query=query.replace('listen','')
            pywhatkit.playonyt(query)
        elif 'open google' in query:
            webbrowser.get(chrome).open("google.com")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is ")
            print(strTime)
            speak(strTime)
        elif 'open movies' in query:
            path="F:\\Telegram movies"
            os.startfile(path)
        elif 'open gmail' in query:
            webbrowser.get(chrome).open("gmail.com")
        elif 'open hackerrank' in query:
            webbrowser.get(chrome).open("hackerrank.com")
        elif 'open meet' in query:
            webbrowser.get(chrome).open("meet.google.com")
        elif 'open classroom' in query:
            webbrowser.get(chrome).open("https://classroom.google.com/u/0/h")
        elif 'java technology lecture' in query:
            webbrowser.get(chrome).open("meet.google.com/khh-vzjd-vyt")
        elif 'software engineering lecture' in query:
            webbrowser.get(chrome).open("meet.google.com/xqp-jcyz-pip")
        elif 'operating system lecture' in query:
            webbrowser.get(chrome).open("meet.google.com/rsd-jqri-avv")
        elif 'design patterns lecture' in query:
            webbrowser.get(chrome).open("meet.google.com/owm-cwiy-vto")
        elif 'language translator lecture' in query:
            webbrowser.get(chrome).open("meet.google.com/emo-guvd-aav")
        elif 'goodbye' in query:
            exit()