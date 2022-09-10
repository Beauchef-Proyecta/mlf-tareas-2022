import time
from client import RobotClient
from inverse_kinematics import position_to_dof
import numpy as np


# Conectarse al robot

r = RobotClient(address="192.168.0.15")  # Recuerda usar una dirección válida
r.connect()
r.home()  # Revisa el archivo client.py para que veas qué hace esta función


# Función para mover el robot usando cartesianas
def move_robot_to_xyz(robot, x, y, z):
    q0, q1, q2 = position_to_dof(x, y, z)
    robot.set_joints(q0, q1, q2)


# Parametrizar un círculo con resolución N
def circle(center, radius, N):
    path = []
    for i in range(N):
        x = radius * np.cos(float(i) / N * 2 * np.pi) + center[0]
        y = radius * np.sin(float(i) / N * 2 * np.pi) + center[1]
        path.append((x, y))
    return path


# Parametrizar un cuadrado con resolución N por lado
def square(center, side, N):
    path = []
    for i in range(N):
        x = center[0] + side * (0.5 - float(i) / N)
        y = center[1] + side * 0.5
        path.append((x, y))

    for i in range(N):
        x = center[0] - side * 0.5
        y = center[1] + side * (0.5 - float(i) / N)
        path.append((x, y))

    for i in range(N):
        x = center[0] - side * (0.5 - float(i) / N)
        y = center[1] - side * 0.5
        path.append((x, y))

    for i in range(N):
        x = center[0] + side * 0.5
        y = center[1] - side * (0.5 - float(i) / N)
        path.append((x, y))

    return path


# Mover el robot
center = (270, 30)
path = square(center, radius=60, N=10)

for x, y in path:
    move_robot_to_xyz(r, x, y, 32)
    time.sleep(0.1)

# Volver al Home al terminar
r.home()
