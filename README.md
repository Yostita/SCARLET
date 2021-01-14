# S.C.A.R.L.E.T.T
Scarlet es una I.A. que por medio del analisis de conversaciones y repetidas interacciones con un usuario intenta simular lo
que para nosotros seria una conversación normal y a su vez puede realizar diversas funciones tales como: la busqueda de datos 
por Internet, ayuda con un codigo, el tiempo en tu zona o un simple calculo matematico.

## Estructura
Este programa esta compuesto por un servidor de DJango.
## Uso
Run
```console
python train.py
```
Esto generara el fichero `data.pth`. Despues ejecutar
```console
python manage.py runserver
```
## Personalizar
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