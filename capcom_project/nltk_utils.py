import numpy as np
import nltk

#La primera vez que se ejecuta hace falta descomentar esto
#nltk.download('punkt')

#from nltk.stem.porter import PorterStemmer
#stemmer = PorterStemmer()

from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('spanish')

def tokenize(sentence):
    """
    Separa la frase en un array de palabras
    """
    return nltk.word_tokenize(sentence)

def stem(word):
    """
    Busca la raiz de la palabra
    Aun por definir para espñaol
    """
    return word.lower()

def bag_of_words(tokenized_sentence, words):
    tokenized_sentence = [stem(word) for word in tokenized_sentence]
    # Inicializamos el array con 0
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in tokenized_sentence:
            bag[idx] = 1

    return bag

''' Test tokenize
a = "Como te llamas?"
print(a)
a = tokenize(a)
print(a)
'''

''' Test stem
a = ["habla", "habladora", "hablador"]
stem_a = [stem(w) for w in a]
print(stem_a)
'''