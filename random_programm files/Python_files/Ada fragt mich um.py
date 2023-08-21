name = input("Wie heißt du?->")
alter = int(input(f"\nSo wie alt bist du {name}?->"))

if alter < 13:
    print("Wirklich, so klein??")
elif 12 < alter < 19:
    print("Du bist immer noch also ein Teenager.")
elif 30 < alter < 60:
    print("Du siehst gar nicht so alt aus.")
elif alter > 80:
    alter = int(input("Ok, nicht lustig, wie alt bist du wirklich?"))
    if 10 < alter < 80:
        print("hmm")
    else:
        print("Das ist mir egal, du Clown.")
else:
    ant = input("Hast du ein Führerschein?")
    if ant.lower() == "ja":
        print("oh supper!")
    else:
        print("hmm")

print("\nJetzt habe ich zwei Fragen, bitte antwort 'ja' order 'nein'")

frage = input("Hast du etwas EDV Kenntnisse: ")
if frage.lower() == "ja":
    print("Super")
else:
    print("Es ist ok, wenn du kein Kenntnisse hast.")

frage = input("\nFreust du dich auf das Bootcamp? ")
if frage.lower() == "ja":
    print("Gut")
else:
    print("Ich bin nicht sicher, warum du hier bist.")

last = input("\nHast du irgendwelche Frage? ")
if last.lower() == "ja":
    q = input("\nFrage: ")
    if q.lower() == "wie heiße ich?" or "wie ist mein name?":
        print(f"Du bist {name}. Danke! Wir sind fertig. Happy coding! :)")
    else:
        print("Ich habe keine Ahnung davon. Danke! Wir sind fertig. Happy coding! :)")
else:
    print("Super, dann wir sind fertig. Danke. Happy coding! :)")
