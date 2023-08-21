import pyttsx3
import time



def say_what(command):
    the_engine = pyttsx3.init()
    voices = the_engine.getProperty('voices')
    # print(voices[1].id)
    the_engine.setProperty('voice', voices[1].id)
    speed=the_engine.getProperty('rate')
    the_engine.setProperty("speed",70)

    the_engine.say(command)
    the_engine.runAndWait()


# saying= f'time right now is {time.ctime(time.time())}'
saying = "Oh hi, I just wanted you to know that I also work offline so you don't have to wqorry hehehe... I mean yes. batti gayo"

say_what(saying)