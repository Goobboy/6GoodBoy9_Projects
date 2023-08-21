import spacy
import time
print("starting")
now = time.time()

nlp = spacy.load("en_core_web_lg")

first = "Have a nice day!"
second = "Enjoy the next 24 hours"

# w1=nlp.vocab[first]
# w2=nlp.vocab[second]

w1 = nlp(first)
w2 = nlp(second)

print(f"similarity: {w1.similarity(w2)}")

print(time.time()- now)