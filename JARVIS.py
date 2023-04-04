import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from googlesearch import search

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
            speak("Good Afternoon")
      else:
            speak("Good Evening!")
             
      speak("Iam Jarvis Sir,Please tell me how may I help you")

def takeCommand():
    #   mic input to string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold=1
         audio=r.listen(source)

    try:
         print("Recognizing...")
         query=r.recognize_google(audio,language='en-in')
         print(f"User said:" ,(query))
    
    except Exception as e:
        
         print("Say that again please...")
         return "None"
    return query

# def sendEmail(to, content):
#     server=smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('',')
#     server

if __name__ == "__main__":
     wishMe()
     while True:
      query=takeCommand().lower()
    #  logic for executing tasks based on query
      if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query=query.replace("wikipedia", "")
        results=wikipedia.summary(query,sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results) 
      elif 'open youtube' in query:
           webbrowser.open("youtube.com")
      elif 'open google' in query:
           webbrowser.open("google.com")
      elif 'open stack overflow' in query:
           webbrowser.open("stackoverflow.com")
      elif 'open code' in query:
          codePath="C:\\Users\\viswa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codePath) 
   

      elif 'play music' in query:
        music_dir ='C:\\Users\\viswa\\OneDrive\\Desktop\\grootan\\songs'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
      elif 'the time' in query:
        strTime= datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,the time is {strTime}")

      elif 'quit' in query:
        exit()
     
    #   elif 'email to viswa' in query:
    #       try:
    #           speak("What should I say?")
    #           content=takeCommand()
    #           to=""
    #           sendEmail(to, content)
    #           speak("Email has been sent!")
    #       except Exception as e:
    #           print(e)
    #           speak("Sorry sir,Iam not able to send this email")

