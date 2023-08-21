import random


def guessthenummer():
    raten = random.randint(1, 100)
    space = "    "

    print("\nGuess the NUMBER between 1 to 100. You have 6 tries!")
    for i in range(6):
        guess = int(input("-> "))

        if guess == raten:
            print("\nOMG YOU DID IT!!!\n\n")
            print("Here is your prize '🥇' ")
            break
        elif guess > raten:
            print("\n", space * 5, "Guesses left:", 5 - i)
            print(f"Number is smaller than {guess}.")
            if i == 5:
                print("\n You lost!!! 👁️👄👁️")
                print(f"correct answer is {raten}")

        elif guess < raten:
            print("\n", space * 5, "Guesses left:", 5 - i)
            print(f"Number is greater than {guess}.")
            if i == 5:
                print("\n You lost!!! 👁️👄👁️")
                print(f"correct answer is {raten}")

if __name__ == "__main__":
    guessthenummer()
