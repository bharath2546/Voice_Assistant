import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib

# microsoft speech api
engine = pyttsx3.init("sapi5")

# inbuilt voices
voices = engine.getProperty("voices")

# set voice  property
engine.setProperty("voices",voices[0].id)


# starter
def wishMe():
    speak("hello, i am your voice assistant")
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("good morning, have a great day")
    elif(hour>=12 and hour<18):
        speak("good afternoon, have a great day")
    else:
        speak("good afternoon have a great day")
    
# query
def takeCommand():
    res = sr.Recognizer()
    with sr.Microphone() as source:
        print("Im listening...")
        res.pause_threshold = 1
        audio = res.listen(source)

    try:
        print("Recognizing....")
        speak("please wait")
        query = res.recognize_google(audio, language="en-in")
        print("User:",query)
        return query
    except:
        print("Im sorry, speak again")
        speak("Im sorry, speak again")
        return "None"


# send email
def sendEmail(to, content):
    server = smtplib.SMTP("smntp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("app@1gmail.com","password")
    server.sendmail("abc@1gmail.com",content)
    server.close()


# speak query
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Activated")
    wishMe()
    while True:
        query = takeCommand().lower()
        if "quit" in query:
            speak("goodbye see you next time")
            break
        elif "wikipedia" in query:
            speak("searching for results")
            query = query.replace("wikipedia", "")
            res = wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            print(res)
            speak(res)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is "+ strTime)
        elif "email to user" in query:
            try:
                speak("what should i do")
                content = takeCommand()
                to="abc@gmails.com"
                sendEmail(to,content)
                speak("email has been sent")
            except:
                speak("email not sent")
        



