import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil 
import pyjokes
import pywhatkit


engine = pyttsx3.init()



# def list_voices():
#     voices = engine.getProperty('voices')
#     for voice in voices:
#         print(f"ID: {voice.id}, Name: {voice.name}, Lang: {voice.languages}")

# def set_voice(voice_id):
#     voices = engine.getProperty('voices')
#     for voice in voices:
#         if voice.id == voice_id:
#             engine.setProperty('voice', voice.id)
#             return 



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# set_voice('HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')  # Example ID

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    day_of_week = now.strftime("%A")  
    speak("The current date is")
    speak(f"Today's date is {day_of_week}, {day} {month} {year}")

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morning sir!")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir")
    elif hour >= 18 and hour<24:
        speak("Good Evening sir")
    else:
        speak("Good night sir")
    speak(" Astra at your service. Please tell me how can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query

    except Exception as e:
        print(e)
        speak("Say that again please..")
        return "None"

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('rajanrp115@gmail.com','Ra11May@n')
        server.sendmail('rajanrp115@gmail.com',to, content)
        server.close()
    except Exception as e:
        print(e)
        speak("Uable to send the email")

def play_song(song):
    try:
        speak(f"Playing {song}...")
        pywhatkit.playonyt(song)
    except Exception as e:
        print(e)
        speak("Uable to play the song")

def screenshot():
    try:
        img = pyautogui.screenshot()
        img.save("C:\\Users\\User\\Desktop\\AI Assistant\\ss.png")
        speak("Done!")
    except Exception as e:
        print(e)
        speak("Uable to take screenshot")

def cpu():
    try:
        usage = str(psutil.cpu_percent())
        speak('CPU is at '+usage)
        battery = psutil.sensors_battery()
        speak("Battery is at")
        speak(str(battery.percent))
    except Exception as e:
        print(e)
        speak("Uable to get CPU usage")

def jokes():
    try:
        joke = pyjokes.get_joke()  
        speak(joke)  
    except Exception as e:
        print(e)
        speak("Uable to get joke")

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences =2)
            print(result)
            speak(result)
        
        
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'soulmoortal@gmail.com'
                sendEmail(to,content)  
                speak(content)
            except Exception as e:
                print(e)
                speak("Uable to send the email")


        elif 'search on chrome' in query or 'search for' in query or 'hey google' in query:
            speak("What should  i search ?")
            search = takeCommand().lower().replace("'", "")  
            url = 'https://www.google.com/search?q=' + search
            os.startfile(url)
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'remember that' in query:
            speak("What should  I remember?")
            data = takeCommand()
            speak("you said me to remember that "+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        
        elif 'do you know anything' in query:
            try:
                remember = open('data.txt','r')
                speak("you said me to remember that "+remember.read())
            except Exception as e:
                print(e)
                speak("I don't remember anything")

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'cpu' in query:
            cpu()

        elif 'play' in query:
            song = query.replace("play", "")
            play_song(song)

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            quit()