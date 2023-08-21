import random
import time

word_list_easy = (
    'ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam',
    'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck',
    'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard',
    'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl',
    'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven',
    'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake',
    'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle',
    'weasel', 'whale', 'wolf', 'wombat', 'zebra' 'buffalo'
)

word_list_hard = (
    'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon',
    'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo',
    'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt',
    'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip',
    'espionage',
    'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby',
    'foxglove',
    'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm',
    'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox',
    'injury',
    'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx',
    'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo',
    'keyhole',
    'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury',
    'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays',
    'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz',
    'pneumonia',
    'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes',
    'quorum',
    'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz',
    'squawk',
    'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless',
    'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown',
    'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway',
    'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy',
    'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee')

# level choose

gnr = '''
                                            HANGMAN!!!
                                    
                    Rule:
                     1) Guess the word by filling the empty gaps with letter.
                     2) You have 5 chances to make mistakes.
                     3) After 6th mistake you will lose.
                     4) If you guess the word before 6th mistake than other mistakes will not count and you will win.
                     
'''

print(gnr)
print("\n\n[ Choose your game mode(1 or 2): ]\n")
time.sleep(.5)
print("1. Animals")
time.sleep(.5)
print("2. Random")
time.sleep(.5)
gamemode = int(input("->"))

body = ("    ",
        " |  ",
        "/|  ",
        "/|\ ",
        "/|\ ",
        "/|\ ")

leg = ("   ",
       "   ",
       "   ",
       "   ",
       "/  ",
       "/ \ ")

l1 = []
badl1 = []
spaces = "       "


def starting(word1):
    for i in range(len(word1)):
        x = word1[i]
        l1.append(x)

    for i in range(len(word1)):
        if random.randint(1, len(word1)) >= ((30 / 100) * len(word1)):
            badl1.append("_")
        else:
            x = word1[i]
            badl1.append(x)

        if badl1.count("_") == len(word1):
            badl1[0] = l1[0]


def turn():
    theword = ""
    for i in range(len(badl1)):
        theword = theword + badl1[i] + " "
    print(theword)


if gamemode == 1:
    word1 = word_list_easy[random.randint(0, 63)]
    length1 = len(word1)
    starting(word1)

    mal = -1
    while True:
        if badl1 == l1:
            print(f"{spaces * 6}YOU JUST WON THIS!!! 🥇")
            print(f"{spaces * 5}   The word was:{word1}")
            break

        turn()
        guess = input(f"Guess a letter:->")

        if guess in l1:
            letters = []
            letters.clear()

            for i in range(len(word1)):
                try:
                    letters.append(word1.index(guess, i, i + 1))
                except:
                    pass

            for i in range(len(letters)):
                badl1[letters[i]] = guess

        elif mal == 4:
            print(
                f"\n{spaces * 15}  +---+\n{spaces * 15}  |   |\n{spaces * 15}  O   |\n{spaces * 15} /|\  |\n{spaces * 15} / \  |\n{spaces * 15}")
            print(f"{spaces * 6}I am sorry, BUT YOU LOST!👎")
            print(f"{spaces * 5}   The word was:{word1}")
            break

        else:
            mal = mal + 1
            time.sleep(0.5)
            print(
                f"\n{spaces * 15}  +---+\n{spaces * 15}  |   |\n{spaces * 15}  O   |\n{spaces * 15} {body[mal]} |\n{spaces * 15} {leg[mal]}  |\n{spaces * 15}      |\n{spaces * 15}=========")



else:
    word1 = word_list_hard[random.randint(0, 202)]
    length1 = len(word1)
    starting(word1)

    mal = -1
    while True:
        if badl1 == l1:
            print(f"{spaces * 6}YOU JUST WON THIS!!! 🥇")
            print(f"{spaces * 5}   The word was:{word1}")
            break

        turn()
        guess = input(f"Guess a letter:->")

        if guess in l1:
            letters = []
            letters.clear()

            for i in range(len(word1)):
                try:
                    letters.append(word1.index(guess, i, i + 1))
                except:
                    pass

            for i in range(len(letters)):
                badl1[letters[i]] = guess

        elif mal == 4:
            print(
                f"\n{spaces * 15}  +---+\n{spaces * 15}  |   |\n{spaces * 15}  O   |\n{spaces * 15} /|\  |\n{spaces * 15} / \  |\n{spaces * 15}")
            print(f"{spaces * 6}I am sorry, BUT YOU LOST!👎")
            print(f"{spaces * 5}   The word was:{word1}")
            break

        else:
            mal = mal + 1
            time.sleep(0.5)
            print(
                f"\n{spaces * 15}  +---+\n{spaces * 15}  |   |\n{spaces * 15}  O   |\n{spaces * 15} {body[mal]} |\n{spaces * 15} {leg[mal]}  |\n{spaces * 15}      |\n{spaces * 15}=========")
