import time
import webbrowser
import random

LernZeit= 8
pause= 10

print("Dein Lernzeit beggint jetzt")

lil=[]

twopel= ("https://www.youtube.com/watch?v=G3lSONLLx70/",
         "https://www.youtube.com/watch?v=h7MYJghRWt0",
         "https://www.youtube.com/watch?v=S2ujotDMluo",
         "https://www.youtube.com/watch?v=O4irXQhgMqg",
         "https://www.youtube.com/watch?v=NW63lS546YQ",
         "https://www.youtube.com/watch?v=J_PCEHjRDtY")

for i in range(4):
    time.sleep(LernZeit)
    webbrowser.open_new("https://www.youtube.com/watch?v=G3lSONLLx70/")
    time.sleep(pause)
    print("Deine Pause ist vorbei")






