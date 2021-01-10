import os
import json
from nltk.tokenize.treebank import TreebankWordDetokenizer

#Reinicia todos los valores de las variables globales
def reset_variables():
    file = open("./static/files/variables_globales", "w")
    file.write("sentimientos;0\n")
    file.write("prueba;0")
    file.close()

#Devuelve el valor de la variable que se le envia como int
def get_valor(variable):
    file = open("./static/files/variables_globales", "r")
    texto = file.readlines()

    if variable == "sentimientos":
        solucion = texto[0].partition(";")[2]
        file.close()
        return int(solucion)
    
    if variable == "prueba":
        solucion = texto[1].partition(";")[2]
        file.close()
        return int(solucion)

#Actualiza la variable que se le envia del fichero variables_globales
def update_variable(variable, nuevoValor):
    file = open("./static/files/variables_globales", "r+")
    texto = file.readlines()

    if variable == "sentimientos":
        # Modificamos la línea que queramos a partir del índice
        texto[0] = "sentimientos;" + str(nuevoValor + get_valor("sentimientos")) + "\n"
    
    if variable == "prueba":
        texto[1] = "prueba;" + str(nuevoValor + get_valor("prueba")) + "\n"

    # Volvemos a ponter el puntero al inicio y reescribimos
    file.seek(0)
    file.writelines(texto)
    file.close()

def update_file_acierto(tag, probabilidad, mensaje):
    #Actualiza su diccionario si no tiene almacenadado ese patron
    with open('intents_sp.json', 'r+') as json_data:
        intents = json.load(json_data)

    for intent in intents['intents']:
        if tag == intent["tag"]:
            if TreebankWordDetokenizer().detokenize(mensaje) not in intent['patterns']:
                intent['patterns'].append(TreebankWordDetokenizer().detokenize(mensaje))
                #Actualiza el json
                with open('intents_sp.json', 'w') as f:
                    json.dump(intents, f, indent=4)

    with open("./static/files/mensajes_acierto", "a") as file:
       file.write(f"{tag} , {probabilidad} , {mensaje}\n")

def update_file_error(tag, probabilidad, mensaje):
    with open("./static/files/mensajes_error", "a") as file:
       file.write(f"{tag} , {probabilidad} , {mensaje}\n")