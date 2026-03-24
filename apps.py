import os
from commands.whatsapp import send_whatsapp_message
from voice import speak, take_command


def open_app(command):

    app = command.replace("open", "").strip()

    try:
        os.system(f"start {app}")
        speak(f"Opening {app}")

    except:
        speak("Application not found")


def run_jarvis():

    while True:

        command = take_command()

        if command == "":
            continue


        # OPEN APPLICATION
        elif "open" in command:
            open_app(command)


        # WHATSAPP MESSAGE
        elif "send whatsapp message" in command:

            speak("Who should I send the message to")

            number = "+91XXXXXXXXXX"

            speak("What should I send")

            message = take_command()

            send_whatsapp_message(number, message)

            speak("Message sent successfully")


        # EXIT
        elif "stop jarvis" in command:

            speak("Goodbye")
            break


if __name__ == "__main__":
    run_jarvis()
