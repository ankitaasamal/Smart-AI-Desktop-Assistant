from cgitb import text

import win32com.client
import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
import datetime


#speaker = win32com.client.Dispatch("SAPI.SpVoice")

#while 1:
 #   print("Enter what you want JARVIS to say")
  ##    speaker.Speak(s)
# todo: teach JARVIS weather api
# todo: teach JARVIS about current affairs

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "I am Sorry. Some error occurred"


if __name__ == '__main__':
    print("PyCharm")
    speak(" Hello I am Jarvis A I , what can I do for you")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"] ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
             speak(f"Sure, opening {site[0]} ma'am...")
             webbrowser.open(site[1])
        if "play some music" in query:
            musicPath = r"C:\Users\KIIT\Desktop\Still with you.mp3"
            speak(f"Sure ma'am,  playing music now ...")
            os.startfile(musicPath)
        if "how are you" in query:
            speak(f"I am doing good, let me know if i can help you")
        if "what are the things that you can do" in query:
            speak(f"I can play music for you....tell you the time......i can open apps for you if you teach me how")
        if "what else" in query:
            speak(f"I can open websites for you or even play a bhajan")

        if "Tony Stark " in query:
            speak(f"No... Ankita did. The JARVIS Tony Stark made turned into Vision..., did you not know that? ")


        elif "the time" in query:
            musicPath = r"C:\Users\KIIT\Desktop\Still with you.mp3"
            #strfTime = datetime.datetime.now().strftime("%H: %M : %S")
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"Ma'am the time is {hour} {min} right now")

        elif "open Brave".lower() in query.lower():
            bravePath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk"
            speak(f"Sure ma'am")
            os.startfile(bravePath)
        elif "Jarvis stop".lower() in query.lower():
            exit()
        elif "Goodbye Jarvis".lower() in query.lower():
            speak(f"I am glad I could help you ma'am. Bye bye")
            exit()
        elif "reset Chat".lower() in query.lower():
            chatStr = ""
        else:
            print("Chatting...")


        #speak(query)