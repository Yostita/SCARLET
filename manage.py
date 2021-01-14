#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import random
import json
import torch
from sentimientos import update_sentimiento
from files_manager import reset_variables, get_valor, update_file_acierto, update_file_error
from model import NeuralNet
from script_manager import script_response
from nltk_utils import bag_of_words, tokenize

reset_variables()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents_sp.json', 'r') as json_data:
    intents = json.load(json_data)

# Cargamos el modelo aprendido
FILE = "data.pth"
data = torch.load(FILE)

# Cargamos Hiperparametros
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


def main():
    """ Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PracticaFinal.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def get_scarlet_renponse(mensaje):
    if mensaje == "quit":
        return 'Adiós putoooo'

    mensaje = tokenize(mensaje)
    x = bag_of_words(mensaje, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x).to(device)

    output = model(x)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                update_file_acierto(tag, prob.item(), mensaje)
                # Comprueba si es una funcion
                if "script" in tag:
                    return script_response(random.choice(intent['responses']))

                update_sentimiento(tag)
                print("Sentimiento actual: " + str(get_valor("sentimientos")))
                return random.choice(intent['responses'])

    update_file_error(tag, prob.item(), mensaje)
    return "Lo siento, no te he entendido"


if __name__ == '__main__':
    main()
