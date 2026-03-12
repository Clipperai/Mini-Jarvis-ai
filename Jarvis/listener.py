import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("Listening...")
        audio = recognizer.listen(source)
        # recognizer.adjust_for_ambient_noise(source)

        # try:
        #     audio = recognizer.listen(source, timeout=5)
        # except:
        #     return None

    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()

        print("You Said:", command)
        return command

    except:
        return None