import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon!!!")
    else:
        speak("Good evening!!!")
    speak("I am jarvis . Please tell me how can I help you")


def takeCommand():
    # it takes microphone the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again plzz...")
        return "None"
    return query


def print_hi(name):
     print(f'Hi, {name}')


if __name__ == "__main__":
    speak("Hey hii")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia..")
            print(results)
            speak(results)
        elif 'open youtube' and 'youtube' and 'play youtube'in query:
            webbrowser.open("Youtube.com")

        elif 'open google' and 'google' and 'go on google'in query:
            webbrowser.open("https://www.google.co.in/")

        elif 'open facebook' and 'fb' and 'facebook' and 'go on fb' and 'go on facebook'in query:
            webbrowser.open("facebook.com")

        elif 'open pinterest' in query:
            webbrowser.open("pinterest.com")

        elif 'play music' in query:
            music_dir = 'D:\SONGS'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
            print(strTime)
        elif 'open code' in query:
            codePath = "C:\\Users\\Sufiya Mulani\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'open xampp' in query:
            codePath = "C:\\xampp\\xampp-control.exe"
            os.startfile(codePath)
        elif 'stop' in query:
            quit()