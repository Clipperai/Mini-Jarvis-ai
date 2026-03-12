from voice import speak
from listener import listen
from commands import run_command

speak("Jarvis activated")

while True:

    command = listen()

    if command is None:
        continue

    if "exit" in command:
        speak("Goodbye")
        break

    run_command(command)