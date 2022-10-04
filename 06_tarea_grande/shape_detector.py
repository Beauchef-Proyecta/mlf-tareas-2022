import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime


class ShapeDetector:
    def __init__(self):
        self.img = None

    def update_image(self, img):
        # Se actualiza la imagen para procesar; se reduce su dimensión, se pasa al espacio RGB y se refleja verticalmente
        self.img = cv2.resize(img, (360, 640))
        self.img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.img = cv2.flip(self.img, 2)

        # Se reinician las matrices auxiliares
        self.img_filtered = np.zeros(img.shape)
        self.img_gray = np.zeros(img.shape)
        self.img_gaus = np.zeros(img.shape)
        self.img_canny = np.zeros(img.shape)
        self.contours = []  # guarda los datos de los contornos

    def process_image(self):
        if self.img is None:
            raise AttributeError("ShapeDetector: 'No tengo una imagen para trabajar:c'")

        # Convertir a escala de grises

        # Filtrar con un Blur Gaussiano
        kernel = (15, 15)

        # Aplicar filtro Canny para detección de bordes

        # Suavizar la imagen con erode y dilate

        # Encontrar contornos

        # Filtrar los contornos obtenidos para quedarse sólo con aquellos cuya área sea suficientemente grande (>10.000px)

        print(f"Contornos detectados: {len(self.contours)}")

    def determine_shape(self):
        if not self.contours:
            # Si no se detectaron contornos relevantes, no se hace nada (sólo se retorna)
            return

        for c in self.contours:
            shape_size = 0

            # Calcular la cantidad de lados de la forma
            """ En esta sección se recomienda consultar el sitio https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/ """

            # Dibujar bounding box del contorno y agregar texto que lo describe
            # OBS: puedes usar libremente el codigo comentado acá abajo, una vez que hayas implementado la parte anterior :)
            # x,y,w,h = cv2.boundingRect(approx)
            # cv2.rectangle(self.img, (x,y), (x+w,y+h), color=(0,255,0), thickness=5)
            # cv2.putText(self.img,'Contorno - '+str(shape_size), (x,y-5),5,2,(0,0,0),thickness = 5)

        return shape_size
