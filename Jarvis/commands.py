from apps import open_app
import webbrowser
import datetime
from voice import speak

def run_command(command):

    if command.startswith("open"):
        open_app(command)

    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")