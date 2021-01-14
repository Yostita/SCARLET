# S.C.A.R.L.E.T.T
Scarlet es una I.A. que por medio del analisis de conversaciones y repetidas interacciones con un usuario intenta simular lo
que para nosotros seria una conversación normal y a su vez puede realizar diversas funciones tales como: la busqueda de datos 
por Internet, ayuda con un codigo, el tiempo en tu zona o un simple calculo matematico.

## Uso
Run
```console
python train.py
```
Esto generara el fichero `data.pth`. Después ejecutamos
```console
python manage.py runserver
```
Al tener control de usuarios hay que loguearse con un usuario y contraseña ya que dependiendo del usuario te trata de una forma diferente.
```console
user: scarlett
psw: @Scarlett1210
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
```

## Estructura y Funcionamiento
Scarlet es una `red neuronal prealimentada`, lo cual quiere decir que las conexiones entre sus unidades no forman un ciclo. En esta red, la información se mueve en una única dirección: adelante. De los nodos de entrada, a través de sus 2 hidden layers hacia los nodos de salida. Al tratarse de una red prealimentada no tiene ninguna forma de aumentar su red mientras esta esté activa por lo que para darle un poco de autonomia hemos creado una funcion la cual aumenta automaticamente su numero de `patterns` con los mensajes del usario que superan el corte de 75% de probabilidad. Gracias a esta función S.C.A.R.L.E.T.T es capaz de poder aumentar considerablemente su analisis de la conversación con el usuario.

![alt text](https://github.com/Yostita/SCARLET/blob/main/Red%20Neuronal.png)

El programa esta compuesto por un servidor hecho en DJango el cual realiza la gestion tanto de usuarios como de mantener activo el portal web en el que se aloja la ventana de chat que se utiliza como input para la I.A. A su vez inicia el escuchador encargado de recibir el mensaje del usario para que este pase por el flujo de analisis de mensaje y mas tarde dar una respuesta.

Algo a destacar es que tambien posee un `sistema de aprendizaje supervisado` el cual consiste en una estructura de ficheros que almacen todos los calculos que realiza mientras esta activa , gestionado por [files_manager.py](files_manager.py) permitiendo asi a los desarrolladores utilizar esta herramienta de aprendizaje para asignarle a su dataset la respuesta correcta a las respuestas que no ha sabido identificar, las que ha acertado no hace falta añadirlas ya que son añadidas automaticamente por el sistema de autoaprendizaje que hablabamos anteriormente.

Por último cuenta con una función de `interpretación de script` la cual analiza si el mesaje que envia el usuario podria ser una petición de alguna de las funciones que ya conoce, de ser asi activaria dicha funcion a traves del gestor de scripts [script_manager.py](script_manager.py) permitiendo asi que S.C.A.R.L.E.T.T pueda servir tambien como `herramienta de busqueda`, `hearramienta de trabajo`, `busqueda de infomación`...
