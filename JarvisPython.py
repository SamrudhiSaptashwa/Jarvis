import time
#import kit as kit
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import wikipedia
import webbrowser
#import cv2
import random
import pyautogui
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from PyQt5.uic import loadUiType
from Jarvis import Ui_JarvisUi
from main import wish

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def wish():
    pyttsx3.speak("Hello...")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        pyttsx3.speak("Good morning!!")
    elif hour >= 12 and hour < 18:
        pyttsx3.speak("Good afternoon!!!")
    else:
        pyttsx3.speak("Good evening!!!")
    pyttsx3.speak("I am Sufiya . Please tell me how can I help you")


# if __name__ == "__main__":
#   pyttsx3.speak("Hey hii sufiya")
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.task()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source,timeout = 5, phrase_time_limit = 10)
            #, timeout = 1, phrase_time_limit = 5

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said:{query}\n")
        except Exception as e:
            pyttsx3.speak("Say that again plzz...")
            return "None"
        return query


    def task(self):
        wish()
        while True:
            self.query = self.takeCommand().lower()
            if 'Wikipedia' in self.query:
                pyttsx3.speak("Searching wikipedia...")
                self.query = self.query.replace("Wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                pyttsx3.speak("According to wikipedia..")
                print(results)
                pyttsx3.speak(results)
            elif 'open youtube' and 'youtube' in self.query:
                webbrowser.open("https://www.Youtube.com/")
            elif 'open google' and 'google' in self.query:
                pyttsx3.speak("what should i search on google")
                cm= self.takeCommand().lower()
                webbrowser.open(f"{cm}")
            elif 'open facebook' and 'facebook' in self.query:
                webbrowser.open("https://www.facebook.com/")
            elif 'open sinhgad website' in self.query:
                webbrowser.open("https://www.sknscoe.ac.in/")
            elif 'open pinterest' in self.query:
                webbrowser.open("https://www.pinterest.com/")
            elif 'open insta' in self.query:
                webbrowser.open("https://www.instagram.com/")
            elif 'open command prompt' and 'open cmd' in self.query:
                os.system("start cmd")
            elif 'play music' in self.query:
                music_dir = "D:\SONGS"
                songs = os.listdir(music_dir)
                rd =random.choice(songs)
                os.startfile(os.path.join(music_dir,rd))
            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                pyttsx3.speak(strTime)
                print(strTime)
            elif 'open code' in self.query:
                codePath = "C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            elif 'open chrome' and 'chrome' in self.query:
                codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(codePath)
            elif 'shutdown' in self.query:
                os.system('shutdown s/ t/ 5')
            elif 'sleep the system' in self.query:
                os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            elif 'switch the window' and 'next window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
            elif 'no thanks' in self.query:
                pyttsx3.speak("Thanks for using me,have a good day")
                quit()

            pyttsx3.speak("do you have any other work")

startExe = MainThread()
class Main(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_JarvisUi()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.startTask)
            self.ui.pushButton_2.clicked.connect(self.close)

        def startTask(self):
            self.ui.movie = QtGui.QMovie("GUI/4.gif")
            self.ui.label.setMovie(self.ui.movie)
            self.ui.movie.start()
            self.ui.movie = QtGui.QMovie("GUI/init sys.gif")
            self.ui.label_2.setMovie(self.ui.movie)
            self.ui.movie.start()
            timer = QTimer(self)
            timer.timeout.connect(self.showTime)
            timer.start(1000)
            startExe.start()

        def showTime(self):
            current_t = QTime.currentTime()
            current_d = QDate.currentDate()
            lable_t = current_t.toString('hh:mm:ss')
            lable_d = current_d.toString(Qt.ISODate)
            self.ui.textBrowser_3.setText(lable_d)
            self.ui.textBrowser_4.setText(lable_t)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

