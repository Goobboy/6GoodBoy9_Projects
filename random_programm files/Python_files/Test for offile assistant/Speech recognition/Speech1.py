import speech_recognition
import pyttsx3

def take_a_command():
    global sth_imp
    #It takes microphone input from the user and returns string output

    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        sth_imp = query
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


while True:
    take_a_command()
    if sth_imp == "exit":
        break
