import speech_recognition as sr
import webbrowser
import sys

r = sr.Recognizer()
#pyinstaller --onefile -w main.py
while True:
    sys.stdout.write('Start')
    data = data = sys.stdin.readline()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        listen = r.listen(source, phrase_time_limit=5)  # Max time limit
        try:
            text:str = r.recognize_google(listen)
            text = "C: "+text
            text = text.replace(" ","\\").lower()
            print(text)
            webbrowser.open(text)
        except:
            print("Error")