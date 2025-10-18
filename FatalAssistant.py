import pyttsx3
import speech_recognition as sr
import webbrowser  
import datetime  
import wikipedia
import pyautogui
print("Version 1.0.0.PUR.1.1.25.PRR.1.2")
print("Hi \n Type \"help\" for a list of commands.")
print("\n This program is best if voice activation is enabled.")
voi = False
print("\nWhat are you waiting for? Start typing!")
def tellTime(self):
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak(self)
    speak("The time is ")
    speak(hour)
    speak("hours and ")
    speak(min)
    speak("minutes")

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1:'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print("The day is " + day_of_the_week)
        speak("The day is " + day_of_the_week)

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
        
        except Exception as e:
            print(e)
            print("Repeat")
            return "None"
        return Query

def Take_query():
    query = takeCommand().lower()
    if "open roblox" in query:
        speak("Opening roblox")
        webbrowser.open("https://www.roblox.com")
        
    elif "new tab" in query:
        speak("Opening new tab")
        webbrowser.open("https://www.google.com")
        
    elif "tell me the time" in query:
        tellTime()
        
    elif "tell me the day" in query:
        tellDay()
        
    elif "open outlook" in query:
        speak("Opening outlook")
        webbrowser.open("https://outlook.com")
        
    elif "open itch" in query:
        speak("Opening itch.io")
        webbrowser.open("https://itch.io")
        
    elif "open discord" in query:
        speak("Opening Discord")
        webbrowser.open("https://discord.com/app")
        
    elif "open gamejolt" in query:
        speak("Opening gamejolt")
        webbrowser.open("https://gamejolt.com")
        
    elif "open playfab" in query:
        speak("Opening Playfab")
        webbrowser.open("https://developer.playfab.com/en-us/my-games")
        
    elif "open scratch" in query:
        speak("Opening Scratch")
        webbrowser.open("https://scratch.mit.edu")
        
        
    elif "search" in query:
        query = query.replace("search", "")
        speak("Going to ")
        speak(query)
        webbrowser.open(query)
        
    elif "from wikipedia" in query:
        speak("Checking the wikipedia")
        query = query.replace("from wikipedia", "")
        result = wikipedia.summary(query, sentences=4)
        speak("According to the wiki")
        print(result)
        speak(result)
        
    elif "tell me your name" in query:
        speak("I am Fatal, an assistant for you")
        print("Fatal")
        
    elif "type" in query:
        speak("Typing")
        query = query.replace("type", "")
        pyautogui.typewrite(query)
        pyautogui.hotkey('enter')
        
    elif "help" in query:
        speak("Printing commands")
        print("Help, you just called this command. \n Open Roblox, opens Roblox in a new tab. \n New Tab, opens a new tab. \n Tell me the time, tells the time. \n Tell me the day, tells you the day. \n Open Outlook, opens Outlook in a new tab. \n Open Itch, opens Itch. \n Open Discord, opens Discord. \n Open GameJolt, opens GameJolt. \n Open Playfab, opens Playfab. \n Open Scratch, opens Scratch. \n Close, closes the program. \n Search (replace with whatever), opens a new tab and searches for what else you said. \n (replace with whatever) from wikipedia, finds the topic around whatever else you said and summarizes the page. \n Open Curseforge, opens Curseforge. \n Type (replace with whatever), types with whatever else you said. \n Text, switches back to text commands. \n Open Github, opens Github.")
        
        
    elif "open forge" in query:
        speak("opening curseforge")
        webbrowser.open("https://www.curseforge.com")
    elif "text" in query:
        speak("Switching to text commands")
        global voi
        voi = False
    elif "open github" in query:
        speak("opening github")
        webbrowser.open("github.com")
    elif "close" in query:
        speak("Adios")
        exit()

def taketype():
    query = input("\n Command: ")
    query = query.lower()
    if "open roblox" in query:
        speak("Opening roblox")
        webbrowser.open("https://www.roblox.com")
        
    elif "new tab" in query:
        speak("Opening new tab")
        webbrowser.open("https://www.google.com")
        
    elif "tell me the time" in query:
        tellTime()
        
    elif "tell me the day" in query:
        tellDay()
        
    elif "open outlook" in query:
        speak("Opening outlook")
        webbrowser.open("https://outlook.com")
        
    elif "open itch" in query:
        speak("Opening itch.io")
        webbrowser.open("https://itch.io")
        
    elif "open discord" in query:
        speak("Opening Discord")
        webbrowser.open("https://discord.com/app")
        
    elif "open gamejolt" in query:
        speak("Opening gamejolt")
        webbrowser.open("https://gamejolt.com")
        
    elif "open playfab" in query:
        speak("Opening Playfab")
        webbrowser.open("https://developer.playfab.com/en-us/my-games")
        
    elif "open scratch" in query:
        speak("Opening Scratch")
        webbrowser.open("https://scratch.mit.edu")
        
        
    elif "search" in query:
        query = query.replace("search", "")
        speak("Going to ")
        speak(query)
        webbrowser.open(query)
        
    elif "from wikipedia" in query:
        speak("Checking the wikipedia")
        query = query.replace("from wikipedia", "")
        result = wikipedia.summary(query, sentences=4)
        speak("According to the wiki")
        print(result)
        speak(result)
        
    elif "tell me your name" in query:
        speak("I am Fatal, an assistant for you")
        print("Fatal")
        
    elif "help" in query:
        speak("Printing commands")
        print("Help, you just called this command. \n Open Roblox, opens Roblox in a new tab. \n New Tab, opens a new tab. \n Tell me the time, tells the time. \n Tell me the day, tells you the day. \n Open Outlook, opens Outlook in a new tab. \n Open Itch, opens Itch. \n Open Discord, opens Discord. \n Open GameJolt, opens GameJolt. \n Open Playfab, opens Playfab. \n Open Scratch, opens Scratch. \n Close, closes the program. \n Search (replace with whatever), opens a new tab and searches for what else you said. \n (replace with whatever) from wikipedia, finds the topic around whatever else you said and summarizes the page. \n Open Curseforge, opens Curseforge. \n Voice, switches to voice commands. \n Open Github, opens Github.")
        
        
    elif "open forge" in query:
        speak("opening curseforge")
        webbrowser.open("https://www.curseforge.com")
    
    elif "voice" in query:
        speak("Switching to voice commands")
        global voi
        voi = True
    elif "open github" in query:
        speak("opening github")
        webbrowser.open("github.com")
    elif "close" in query:
        speak("Adios")
        exit()

while True:
    if __name__ == '__main__':
        if voi:
            Take_query()
        else:
            taketype()
