# Libreria que asigna un valor positivo o negativo a cada tag
from files_manager import update_variable

'''
    TODO se deberia hacer un fichero que alamcenase el valor de los sentimientos y que esta funcion
    simplemente leyese de ese fichero su valor

    TODO se podria utilizar un array de valores de sentimientos en vez de una sola variable para poder
    jugar tambien con la personalidad
'''


def update_sentimiento(tag):
    if tag == "cumplido":
        update_variable("sentimientos", 2)
    if tag == "insulto":
        update_variable("sentimientos", -3)
    if tag == "prueba":
        update_variable("prueba", 1)
