import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pandas as pd
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

hour = int(datetime.datetime.now().hour)
strTime = datetime.datetime.now().strftime("%H:%M:%S")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello My name is Optimus Prime. Sir Faizan! How may I help you")

def reminder():
    strTime = datetime.datetime.now()

    if strTime == strTime.replace(hour=17,minute=2):
        speak("Reminder! It's your medicine time, I'm repeating it's your medicine time")
        speak("Reminder! It's your medicine time, I'm repeating it's your medicine time")
    elif strTime == strTime.replace(hour=17,minute=1):
        speak("Reminder! It's lunch time, Just eat your lunch before times up")

def takeCommand0():
    '''It Takes microphone input from the user'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:

        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print("I don't get it Sir....")
        #speak("I don't get it Sir....")
        return "None"
    return query

def takeCommand():
    '''It Takes microphone input from the user'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:

        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        
        print("Say that again please....")
        speak("Say that again please....")
        return "None"
    return query


def takeCommand1():
    '''It Takes microphone input from the user'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:

        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print("I don't get it Sir....")
        speak("I don't get it Sir....")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()

    while True:

        reminder()
        start = takeCommand0().lower()

        if 'prime' in start:
            speak('Yes Sir')
            query = takeCommand().lower()


            query = query.replace('prime', '')
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace('wikipedia','')
                chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                #speak("what do you want to search")
                #query1 = takeCommand1().lower()
                webbrowser.get('chrome').open_new_tab(f'wikipedia.com/wiki/' + query)
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'search' in query:
                query = query.replace('open', '')
                chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                speak("what do you want to search")
                query1 = takeCommand1().lower()
                webbrowser.get('chrome').open_new_tab('google.com/?#q=' + query1)

            elif 'open youtube' in query:
                query = query.replace('open', '')
                chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                speak("what do you want to search")
                query1 = takeCommand1().lower()
                webbrowser.get('chrome').open_new_tab(f'{query}.com/results?search_query=' + query1)

            elif 'video' in query:
                query = query.replace('video of', '')

                browser = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
                browser.get('https://www.youtube.com/results?search_query=' + query)
                element = browser.find_element_by_xpath('// *[ @ id = "img"]')
                element.click()

            elif 'play' in query:
                #if 'The Walking Dead' in query:
                query = query.replace('play the walking dead season', '')
                query = query.replace(" ","")
                series_dir = f'F:\\series\\The-Walking-Dead-S0{query}'
                episodes = os.listdir(series_dir)
                print(episodes)
                speak('Which Episode do you want play? Sir!')
                query1 = takeCommand1().lower()
                if 'episode' in query1:
                    query2 = query1.replace('episode', '')
                    query3 = query2.replace(" ", "")
                    query5 = int(query3)
                    s = query5-1
                    print(type(s))
                    print(s)
                    os.startfile(os.path.join(series_dir, episodes[s]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open vs code' in query:
                Path = "C:\\Users\\ITSM\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(Path)

            elif 'open pycharm' in query:
                Path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.4\\bin\\pycharm64.exe"
                os.startfile(Path)

            elif 'open spyder' in query:
                Path = "C:\\Users\\ITSM\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Spyder (anaconda)"
                os.startfile(Path)

            elif 'open jupyter notebook' in query:
                Path = "C:\\Users\\ITSM\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Jupyter Notebook (anaconda)"
                os.startfile(Path)

            elif 'open c drive' in query:
                Path = "C:\\"
                os.startfile(Path)

            elif 'open d drive' in query:
                Path = "D:\\"
                os.startfile(Path)

            elif 'open E drive' in query:
                Path = "D:\\"
                os.startfile(Path)

            elif 'open downloads' in query:
                Path = "C:\\Users\\ITSM\\Downloads"
                os.startfile(Path)

            elif 'open control panel' in query:
                Path = "C:\\Users\\ITSM\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel"
                os.startfile(Path)

            elif 'open teams' in query:
                Path = "C:\\Users\\ITSM\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams.lnk"
                os.startfile(Path)

            elif 'open ms word' in query:
                Path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013.lnk"
                os.startfile(Path)

            elif 'open excel' in query:
                Path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013.lnk"
                os.startfile(Path)

            elif 'open power point' in query:
                Path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013.lnk"
                os.startfile(Path)

            elif 'open skype' in query:
                Path = "C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe"
                os.startfile(Path)

            elif 'open opera' in query:
                Path = "C:\\Users\\ITSM\\AppData\\Local\\Programs\\Opera\\launcher.exe"
                os.startfile(Path)

            elif 'open proteus' in query:
                Path = "C:\\Program Files (x86)\\Labcenter Electronics\\Proteus 8 Professional\\BIN\\PDS.EXE"
                os.startfile(Path)

            elif 'drive' in query:
                Path = "C:\\Users\\ITSM\\Google Drive"
                os.startfile(Path)

            elif 'open task manager' in query:
                Path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.lnk"
                os.startfile(Path)

            elif 'not feeling well' or 'sick' in query:

                    speak("oh Take care sir take necessary precautions and eat well to stay energetic")

