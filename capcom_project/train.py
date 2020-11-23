import json
from nltk_utils  import  tokenize, stem, bag_of_words

with open('intents_sp.json','r') as f:
    intents = json.load(f)

all_words = []
tags = []
#Aun por definir
xy= []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        p = tokenize(pattern)
        all_words.extend(p)
        xy.append((p,tag))

ignore_words = ['?', '!', '.', ',']
all_words = [stem(w) for w in all_words if w not in ignore_words]
print(all_words)