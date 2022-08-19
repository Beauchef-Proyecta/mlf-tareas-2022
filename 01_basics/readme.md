# Tarea 1 - Un robot en la vida real 🦾

Esta tarea tiene 2 objetivos principales:
1. Que tengas todas las herramientas de software que usaremos en el curso instaladas en tu computador
2. Que muevas un robot nuestra *Pequeña Fábrica:tm:* :fire:

## Parte 1: Instalar todo

Revisa las instrucciones de instalación de las herramientas en la [wiki de este repositorio](https://github.com/Beauchef-Proyecta/mlf-base/wiki/Instalaci%C3%B3n-de-Herramientas-de-Software).

Si tienes cualquier problema, contacta a tus auxiliares :)

Una vez que esté todo instalado, abre el archivo `01_basics/test.py` y córrelo. Si en la consola se imprime "Todo perfectamente instalado :ok_hand:" puedes pasar a la parte 2.


## Parte 2: Mover un robot


### ¿Cómo funciona la *Pequeña Fábrica:tm:* ?
La *Pequeña Fábrica:tm:* está compuesta por 8 brazos robotizados con 3 articulaciones cada uno. Cada articulación se mueve gracias a un motor servo, que a su vez es controlado por una placa Arduino Nano. 

El Arduino Nano tiene recursos computacionales limitados, por lo que necesitamos un computador un más potente si queremos que nuestra fábrica pueda hacer tareas mas complejas y, mas importante que eso, en una red de internet. En este caso usamos un micro-computador Raspberry Pi 4 por cada brazo que controla su respectiva placa Arduino y mantiene una conexión de *red de área local* (LAN).

Esto permite que, si estás en la misma red que la *Pequeña Fábrica:tm:*, puedes enviarle instrucciones desde tu computador para mover alguno de los motores. Para enviar estas instrucciones usaremos Python y sus librerías.

### Ok, ahora vamos al código

El código de esta tarea tiene varios archivos y cada uno se encarga de algo en particular:

- **`move_the_robot.py`**

    Este es el archivo donde escribirás los comandos para mover el robot


- **`client.py`**
    Archivo con una clase que nos ayuda a enviar las instrucciones a través de la red.
    
    *No edites este archivo*

- **`mock_server.py`**
    ¿Cómo probamos que nuestro código en `move_the_robot.py` está enviando todo bien? Hacemos un *servidor falso*. Este archivo contine una copia de la lógica que está en la Raspberry Pi del robot, pero que no mueve nada y lo corremos en nuestro computador.
    
    *No edites este archivo*
    

### Escribamos nuestras primeras instrucciones

En Pycharm, abre la carpeta como un proyecto, así se verán todos los archivos.

Luego, abre `move_the_robot.py`. Debería lucir así:

```python
import time
from .client import RobotClient


## Conectarse al robot

robot = RobotClient(address="")  # Recuerda usar una dirección válida
robot.connect()

## Mover el robot (acá va tu código)

    ...
```

Las primeras 2 líneas se encargan de importar 2 dependencias: `time`, para poder hacer pausas (`time.sleep`) y `client`, a partir del archivo `client.py` de esta tarea y que contiene una clase `RobotClient`.

La clase `RobotClient` permite conectarse a un robot especificando su dirección IP. Probemos cómo funciona esto usando el servidor falso:

1. Abre el archivo `mock_server.py` en una nueva pertaña y córrelo. Fíjate que el *servidor falso* quedó ligado a la dirección `172.0.0.1` (o `localhost`)
2. Vuelve al archivo `move_the_robot.py` y reemplaza `address=""` por `address="localhost"`. Esto hará que `RobotClient` se conecte al servidor falso.
3. Corre el archivo `move_the_robot.py`. ¿Qué vez en la consola?




    
