# ----------------------------------------------------------------------------------------------------------------------

import os
import cv2 as cv

# ----------------------------------------------------------------------------------------------------------------------


class Conversor:

    @staticmethod
    def guardar_imagen(ruta_img_pgm):

        img_pgm = cv.imread(ruta_img_pgm, 0)
        ruta, nombre = os.path.split(ruta_img_pgm)
        nombre = os.path.splitext(nombre)[0] + ".png"
        ruta_imagen_png = os.path.join(ruta, nombre)
        cv.imwrite(ruta_imagen_png, img_pgm)

    @staticmethod
    def convertir_pgm_a_png(ruta_img_pgm):

        ruta, nombre = os.path.split(ruta_img_pgm)
        nombre = os.path.splitext(nombre)[0] + ".png"
        ruta_imagen_png = os.path.join(ruta, nombre)

        return ruta_imagen_png

# ----------------------------------------------------------------------------------------------------------------------
