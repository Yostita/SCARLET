# S.C.A.R.L.E.T.T
Scarlet es una I.A. que por medio del analisis de conversaciones y repetidas interacciones con un usuario intenta simular lo
que para nosotros seria una conversación normal y a su vez puede realizar diversas funciones tales como: la busqueda de datos 
por Internet, ayuda con un codigo, el tiempo en tu zona o un simple calculo matematico.

## Estructura
Scarlet es una red neuronal prealimentada, lo cual quiere decir que las conexiones entre sus unidades no forman un ciclo. En esta red, la información se mueve en una única dirección: adelante. De los nodos de entrada, a través de sus 2 hidden layers hacia los nodos de salida.

El programa esta compuesto por un servidor hecho en DJango el cual realiza la gestion tanto de usuarios como de mantener activo el portal web en el que se aloja la ventana de chat que se utiliza como input para la I.A. 

## Uso
Run
```console
python train.py
```
Esto generara el fichero `data.pth`. Después ejecutamos
```console
python manage.py runserver
```
## Personalización
Si analizamos [intents_sp.json](intents_sp.json). Se pueden editar las respuestas de S.C.A.R.L.E.T.T. Simplemente define un nuevo `tag`, posibles `patterns`, y posibles `responses`. Tienes que volver a ejecutar el entrenamiento para que se guarden las modificaciones.
```console
{
  "intents": [
    {
      "tag": "nota",
      "patterns": [
        "que nota crees que se merecen estos chicos?",
        "que nota le deberia poner a estos buenos hombres"
      ],
      "responses": [
        "Segun mis calculos la nota correspondiente a su esfuero es... Un 10.
      ]
    },
    ...
  ]
}
