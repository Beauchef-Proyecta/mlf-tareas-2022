import numpy as np
import random

from transformations import (
    translation_along_zaxis,
    rotation_around_zaxis,
    rotation_around_yaxis,
)


class MK2Robot:
    HOME_0 = 0
    HOME_1 = 0
    HOME_2 = 90

    def __init__(self):
        self.a = [55, 39, 135, 147, 66.3]
        self.q = []
        self.T = []
        self.pose = []

        # Cada commando se asocia con un método de esta clase. Cada método ejecuta un tipo de movimiento
        self.command_action = {
            "3": self.move_right,
            "4": self.move_left,
            "5": self.movimiento_que_debes_implementar,
        }

        self.update_pose(MK2Robot.HOME_0, MK2Robot.HOME_1, MK2Robot.HOME_2)

    def execute(self, command=None, text=None):
        if not command:
            return

        if command not in self.command_action:
            print("MK2Robot: 'Recibí un comando, pero no sé que tengo que hacer'")
            return

        # Si se recibe un comando, se ejecuta la función a la que está mapeada (ojo con los paréntesis al final)
        self.command_action[command]()
        print(text)

    def move_left(self):
        """Toma la posición actual y gira 5 grados hacia la izquierda"""
        # IMPLEMENTAME

    def move_right(self):
        """Toma la posición actual y gira 5 grados hacia la derecha"""
        # IMPLEMENTAME

    # Adicionalmente, debes implementar un movimiento adicional (como a ti te guste)
    def movimiento_que_debes_implementar(self):
        print("hago cositas jijijiji")
        # IMPLEMENTAME

    # De aquí en adelante es código de la tarea 2 :)
    def update_pose(self, q0, q1, q2):
        """
        Este metodo calcula la pose de cada link del robot, usando las matrices T y R. Luego guarda el
        resultado para cada link como un elemento del arreglo self.pose
        """
        # Calcula las matrices T y Q
        self.calculate_transformation_matrices(q0, q1, q2)

        # re-escribe self.pose como una lista de 4 matrices nulas
        self.pose = [np.zeros((4, 4))] * 4

        self.pose[0] = np.linalg.multi_dot([self.T[0], self.R[0], self.T[1]])
        self.pose[1] = np.linalg.multi_dot([self.pose[0], self.R[1], self.T[2]])
        self.pose[2] = np.linalg.multi_dot([self.pose[1], self.R[2], self.T[3]])
        self.pose[3] = np.linalg.multi_dot([self.pose[2], self.R[3], self.T[4]])

    def calculate_transformation_matrices(self, q0, q1, q2):
        """
        Este método calcula las matrices de rotación traslación del modelo de nuestro robot
        y guarda sus valores como elementos de las listas self.R y self.T, en orden
        """
        q0 = q0 * np.pi / 180
        q1 = q1 * np.pi / 180
        q2 = q2 * np.pi / 180

        self.q = [q0, q1, q2]

        self.T = []
        self.R = []

        angulo_rotacion_l0 = q0
        angulo_rotacion_l1 = q1
        angulo_rotacion_l2 = -np.pi + q2
        angulo_rotacion_l3 = np.pi / 2 - q1 - q2

        # Link 1
        self.T.append(translation_along_zaxis(self.a[0]))
        self.R.append(rotation_around_zaxis(angulo_rotacion_l0))

        # Link 2
        self.T.append(translation_along_zaxis(self.a[1]))
        self.R.append(rotation_around_yaxis(angulo_rotacion_l1))

        # Link 3
        self.T.append(translation_along_zaxis(self.a[2]))
        self.R.append(rotation_around_yaxis(angulo_rotacion_l2))

        # Link 4
        self.T.append(translation_along_zaxis(self.a[3]))
        self.R.append(rotation_around_yaxis(angulo_rotacion_l3))

        # Link 5
        self.T.append(translation_along_zaxis(self.a[4]))

    def current_joint_positions(self):
        """Este método entrega las coordenadas de cada joint en tres listas; es para que el codigo se vea mas limpio :)"""
        X_pos = np.zeros(4)
        Y_pos = np.zeros(4)
        Z_pos = np.zeros(4)

        for i in range(len(self.pose)):
            X_pos[i] = np.round(self.pose[i][0, 3], 3)
            Y_pos[i] = np.round(self.pose[i][1, 3], 3)
            Z_pos[i] = np.round(self.pose[i][2, 3], 3)

        return [X_pos, Y_pos, Z_pos]
