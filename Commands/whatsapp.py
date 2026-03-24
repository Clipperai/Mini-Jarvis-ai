import pywhatkit as kit
import time

def send_whatsapp_message(number, message):

    try:
        kit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)

        print("Message sent successfully")

    except Exception as e:
        print("Error:", e)
