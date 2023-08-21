import spacy
import time

print("strating")
n = time.time()
nlp = spacy.load("en_core_web_lg")

sentences_dict_1= {
    "How are you doing?": "How's it going?",
    "I'm really tired today.": "I feel exhausted today.",
    "Can you please help me with this task?": "Could you lend me a hand with this job?",
    "Let's grab a bite to eat.": "How about we get some food?",
    "It's such a beautiful day outside!": "The weather is fantastic today!",
    "I had a great time at the party.": "The party was so much fun!",
    "I need to buy some groceries.": "I have to get some supplies from the store.",
    "I'm sorry for the inconvenience.": "I apologize for any trouble caused.",
    "Can we reschedule the meeting?": "Is it possible to move the meeting to another time?",
    "Thanks for your help!": "I appreciate your assistance!"
}

sentences_dict_2 = {
    "The sun is shining brightly.": "The weather is pleasant.",
    "She sings beautifully.": "Her voice is melodious.",
    "He runs fast.": "He moves quickly.",
    "The flowers smell delightful.": "The flowers have a pleasant aroma.",
    "The baby is giggling.": "The baby is laughing joyfully.",
    "We had a great time at the beach.": "We enjoyed ourselves at the seaside.",
    "The dog is barking loudly.": "The dog is making a loud noise.",
    "He is wearing a red shirt.": "He has a red shirt on.",
    "The cake looks delicious.": "The cake appears appetizing.",
    "The car is parked in the garage.": "The car is in the garage.",
    "She is laughing uncontrollably.": "She can't stop laughing.",
    "The music sounds soothing.": "The music is calming.",
    "The bird is chirping.": "The bird is singing.",
    "They are having a picnic.": "They are enjoying a picnic.",
    "I play the guitar.": "I'm skilled at playing the guitar.",
    "He is telling jokes.": "He's sharing jokes.",
    "The stars are shining in the sky.": "The stars are twinkling above.",
    "We visited a museum today.": "We went to a museum.",
    "The children are playing games.": "The kids are gaming.",
    "She is baking cookies.": "She's making cookies.",
    "The movie was entertaining.": "The movie was enjoyable.",
    "The train is arriving soon.": "The train will be here soon.",
    "The dog is fetching a ball.": "The dog is retrieving the ball.",
    "He enjoys playing soccer.": "He loves playing soccer.",
    "We had a delicious dinner.": "The dinner was delectable.",
    "The mountain looks majestic.": "The mountain appears grand.",
    "She is drawing a picture.": "She's sketching an image.",
    "The ocean waves crash.": "The waves are crashing.",
    "The pen writes smoothly.": "The pen glides smoothly.",
    "The tree sways in the wind.": "The tree moves in the wind.",
    "The car engine roars.": "The engine emits a roaring sound.",
    "The raindrops fall gently.": "The raindrops are falling gently.",
    "The stars twinkle in the sky.": "The stars are sparkling.",
    "The baby is crawling.": "The baby crawls on the floor.",
    "The clock chimes noon.": "The clock strikes twelve.",
    "The cake smells heavenly.": "The cake has a heavenly aroma.",
    "The airplane soars high.": "The airplane flies high.",
    "The fire crackles and pops.": "The fire is crackling and popping.",
    "The waves crash on the shore.": "The waves are crashing on the beach.",
    "The balloon floats away.": "The balloon is floating upwards.",
    "The keys jingle in my pocket.": "The keys make a jingling sound.",
    "The wind rustles the leaves.": "The wind is rustling the leaves.",
    "The baby cries softly.": "The baby is crying softly.",
    "The computer screen glows.": "The computer screen is glowing.",
    "The bicycle tires spin.": "The bicycle tires are spinning.",
    "The door creaks open.": "The door is creaking open.",
    "The water trickles down the stream.": "The water is trickling in the stream.",
    "The phone vibrates in my hand.": "The phone is vibrating.",
    "The moonlight illuminates the night.": "The moonlight lights up the night.",
    "The leaves crunch underfoot.": "The leaves are crunchy underfoot.",
    "The baby laughs joyfully.": "The baby is laughing with joy."
}

sentences_dict = {
    "The sun is radiating brilliantly.": "I adore indulging in ice cream.",
    "She possesses an exquisite singing voice.": "The cat is slumbering serenely.",
    "He sprints with exceptional speed.": "My favored hue is indigo.",
    "The blossoms emit an enchanting fragrance.": "They are frolicking in the park.",
    "The infant emits gleeful laughter.": "The coffee exudes a bitter taste.",
    "We relished an extraordinary day at the seaside.": "The book captivated my attention.",
    "The canine vocalizes loudly.": "She moves gracefully on the dance floor.",
    "He adorns a scarlet attire.": "I derive great pleasure from watching films.",
    "The cake's appearance is delectable.": "Precipitation is occurring outdoors.",
    "The automobile is stationed in the garage.": "I derive enjoyment from perusing novels.",
    "She is in the throes of uncontrollable laughter.": "He diligently prepares for the examination.",
    "The music has a calming effect.": "We embarked on an excursion in the mountains.",
    "The avian creature emits a melodious song.": "The river exhibits a swift current.",
    "They are partaking in a picnic gathering.": "The pizza boasts exceptional flavor.",
    "I am skilled at playing the guitar.": "She adeptly creates artful compositions.",
    "He entertains with humorous anecdotes.": "I have a preference for tea over coffee.",
    "The stars are brilliantly shimmering in the celestial expanse.": "The laptop is pristine and new.",
    "We explored the exhibits at the museum today.": "The clock is incessantly ticking away.",
    "The youngsters are engrossed in playing games.": "I derive pleasure from swimming in the pool.",
    "She is occupied with baking delicious cookies.": "He is operating a blue-colored automobile.",
    "The movie provided an enjoyable experience.": "I derive immense pleasure from beach visits.",
    "The train's arrival is imminent.": "They are embarking on a journey."
}


print(time.time()-n)
average = 0
counter = 0

def testing():
    global average, counter
    for key in sentences_dict.keys():
        counter = counter+1
        the_timer = time.time()

        print(f'{key} -> {sentences_dict.get(key)}\n->')

        w1 = nlp(key)
        w2 = nlp(sentences_dict.get(key))
        print(f"similarity: {w1.similarity(w2)}")

        average = average + w1.similarity(w2)

        print(f"time take: {time.time() - the_timer}\n")


testing()

print(f'average similarity: {average/counter}')
