import time
from client import RobotClient
from inverse_kinematics import position_to_angles


## Conectarse al robot

r = RobotClient(address="localhost")  # Recuerda usar una dirección válida
r.connect()
r.home()    # Revisa el archivo client.py para que veas qué hace esta función


## Función para mover el robot usando cartesianas
def move_robot_to_xyz(robot, x, y, z):
    q0, q1, q2 = position_to_angles(x, y, z)
    robot.set_joints(q0, q1, q2)


## Mover el robot (acá va tu código)
move_robot_to_xyz(r, x=200, y=0, z=230)



