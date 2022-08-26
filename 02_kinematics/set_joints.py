import time
from client import RobotClient


## Conectarse al robot

robot = RobotClient(address="localhost")  # Recuerda usar una dirección válida
robot.connect()

## Mover el robot (acá va tu código)

HOME_Q0 = 0
HOME_Q1 = 0
HOME_Q2 = 90

robot.set_joints(q0=HOME_Q0, q1=HOME_Q1, q2=HOME_Q2)
time.sleep(2)
robot.set_joints(q0=45, q1=30, q2=80)

