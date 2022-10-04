import cv2
import matplotlib.pyplot as plt
import numpy as np

from shape_detector import ShapeDetector
from decision_manager import DecisionManager
from mk2_model import MK2Robot
from plotter import Plotter


def main():

    """[1. Inicialización]"""
    camera = cv2.VideoCapture(1)  # Por defecto es 0
    detector = ShapeDetector()
    manager = DecisionManager()
    robot = MK2Robot()
    plotter = Plotter()

    """ [2. Loop Infinito] """
    while plotter.is_enabled():

        # 1. Capturar imagen
        _, frame = camera.read()

        # 2. Procesar
        detector.update_image(frame)
        detector.process_image()
        shape = detector.determine_shape()

        # 3. Decidir
        command, text = manager.decide_what_to_do(shape)

        # 4. Actuar
        robot.execute(command, text)

        # 5. Mostrar resultado
        processed_image = detector.img
        robot_pose = robot.current_joint_positions()
        plotter.update(img=processed_image, robot=robot_pose)

    # Una vez que se cierra el plot, se destruye todo para tener una salida limpia :)
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
