import time
from client import RobotClient


## Conectarse al robot

robot = RobotClient(address="localhost")  # Recuerda usar una dirección válida
robot.connect()

## Mover el robot (acá va tu código)

robot.move_xyz(x=10, y=12, z= 90)
robot.move_xyz(x=15, y=14, z= 90)
robot.move_xyz(x=60, y=20, z= 90)
