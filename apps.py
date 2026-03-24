import os
from voice import speak

def open_app(command):

    command = command.replace("open","")

    try:
        os.system(f"start {command}")
        speak(f"Opening {command}")

    except:
        speak("Application not found")