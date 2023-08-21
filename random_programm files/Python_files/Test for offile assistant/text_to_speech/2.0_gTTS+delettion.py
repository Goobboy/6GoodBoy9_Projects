from gtts import gTTS
import os
from playsound import playsound
import time


def speak(the_text):
    text_to_speech = gTTS(text=the_text, tld='en.ie', lang='en',  slow=False)
    text_to_speech.save('thetext.mp3')
    try:
        time.sleep(0.7)
        playsound('thetext.mp3')
    except:
        time.sleep(0.7)
        playsound('thetext.mp3')

    if os.path.exists("thetext.mp3"):
        os.remove("thetext.mp3")
        print("deleted")
    else:
        print("The file does not exist")

to_say= input("what to say?\n->")

speak(to_say)