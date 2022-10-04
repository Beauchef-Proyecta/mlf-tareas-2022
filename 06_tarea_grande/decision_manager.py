class DecisionManager:
    """
    Esta clase sólo se preocupa de decidir qué tiene que hacer el robot
    para cada caso detectado.
    """

    def __init__(self):

        # Cada posible entrada (shape) se 'mapea' con un determinado texto que indica lo que el robot debe hacer
        self.commands = {
            "3": "Mover robot derecha",
            "4": "Mover robot izquierda",
            "5": "Mover robot arriba",
            "6": "Mover robot abajo",
        }

    def decide_what_to_do(self, shape):
        """
        La lógica implementada en esta clase es sencilla, pero en general se pueden usar
        algoritmos de mayor complejidad para analizar qué es lo mejor a hacer en cada caso.

        De momento, sólo entrega un comando que es igual a la entrada que recube (shape), además del texto
        que acompaña al comando.
        """
        shape = str(shape)
        if shape not in self.commands:
            # Si no se entrega una forma, se devuelve un comando nulo y un texto que lo indica
            return None, "no sé qué hacer :c"

        return shape, self.commands[shape]
