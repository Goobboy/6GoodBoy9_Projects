import random
import time
import webbrowser

stunde = float(input("How many hour you want to study?(for example: 3.5)\n->"))
insec = stunde*60*60

spaces="      "

LernZeit = float(input("How long study time you want?(In minutes)\n->"))
LernZeit= LernZeit*60
pause = float(input("How long breaks do you want?(In  minutes)\n->"))
pause = pause*60

now = (time.ctime())
then = (time.ctime(time.time() + insec))

print(now)
print(then)

twopel= ("https://www.youtube.com/watch?v=G3lSONLLx70/",
         "https://www.youtube.com/watch?v=h7MYJghRWt0",
         "https://www.youtube.com/watch?v=S2ujotDMluo",
         "https://www.youtube.com/watch?v=O4irXQhgMqg",
         "https://www.youtube.com/watch?v=NW63lS546YQ",
         "https://www.youtube.com/watch?v=J_PCEHjRDtY",
         "https://www.youtube.com/watch?v=m4ZcTU43Anc")

chutti = 0.0
padhai= 0.0

print("\n\n[ Dein Lernzeit beggint jetzt!!! ]\n")

while True:
    time.sleep(LernZeit)
    print("( Dein Pause beggint nach 3 Sekunden! ) ")
    time.sleep(3)

    webbrowser.open_new(twopel[random.randint(0,6)])
    time.sleep(pause)

    chutti = chutti+1
    print("{ Deine Pause ist vorbei! }")

    print("_____________________________________________________________")

    print("\n~ Beginn mit deiner Arbeit! ~")
    padhai = padhai+ (pause*60)
    print(f"{spaces*5} Insgesamt Arbeitszeit: {padhai} minuten")
    print(f"{spaces * 5} Break counter: {chutti} mal")

    if then < now:
        print("_______________Your study time is finished_______________")
        break

