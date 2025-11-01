import speech_recognition as sr
import musicLibrary
import webbrowser
import pyttsx3
from gtts import gTTS

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()  
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open whatsApp" in c.lower():
        webbrowser.open("https://whatsApp.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        Link=musicLibrary.music[song]

        webbrowser.open(Link)
     


    print(c)
if __name__ == "__main__":
    speak("Initializing jarvis......")
    while True:
            # Listen for the wake word "Jarvis"
            # obtain audio from the microphone
         r = sr.Recognizer()

            # recognize speech using Sphinx
         print("recognizing.....")
         try:
           with sr.Microphone() as source:
                 print("listening.....")
                 audio = r.listen(source, timeout=5, phrase_time_limit=5)
                 word = r.recognize_google(audio)

                 if( word.lower() == "jarvis"):
                  speak("Ya")
                  # listening for command
                  with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command= r.recognize_google(audio)
                    processCommand(command)

         except Exception as e:
                print("Error: Apne kuch bola nehi... {0}".format(e))