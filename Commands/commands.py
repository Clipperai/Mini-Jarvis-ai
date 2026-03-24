from apps import open_app
import webbrowser
import datetime
from voice import speak

def run_command(command):
    if command.startswith("open"):
        open_app(command)
    
    elif "hello" in command:
        speak("Hello Sir, how can I assist you?")

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening Youtube")

    elif "google" or "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "time" or "show time" in command:
        now = datetime.datetime.now()
        print("The Current time is " + now.strftime("%H:%M"))
        speak("The Current time is " + now.strftime("%H:%M"))

    elif "search" in command:
        search_query = command.replace("search", "")
        webbrowser.open("https://www.google.com/search?q=" + search_query)
        speak("Searching for " + search_query)
    
    else:
        speak("Sorry, I didn't understand that command.")
