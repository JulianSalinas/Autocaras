# ----------------------------------------------------------------------------------------------------------------------

import glob
import os

import cv2 as cv
import numpy as np

from controlador.configuracion import *


# ----------------------------------------------------------------------------------------------------------------------


class Coleccion(object):

    def __init__(self):

        """
        Encargada de proporcionar las rutas de cada una de las imagenes presentes en la base de datos, asi como otra
        información importante, como la cantidad de sujetos, la cantidad de imagenes totales y por sujeto junto con la
        resolucion de cada una. Sirve para encontrar el sujeto con el que coincide una imagen al momento de clasificar
        """

        self.dic_sujs = {}
        self.dic_imgs = {}
        self.obt_diccionarios()

        self.alto_img = 0
        self.ancho_img = 0
        self.obt_dimensiones()

        self.total_sujs = len(self.dic_sujs)
        self.total_imgs = len(self.dic_imgs)
        self.pixeles_img = self.ancho_img * self.alto_img

    # ------------------------------------------------------------------------------------------------------------------

    def consultar_img(self, indice_img):

        """
        Obtiene la ruta de la imagen según el índice obtenido de la matriz de imagenes de la colección
        @param indice_img: Índice devuelto por el clasificador
        @return: ruta_suj, ruta_img
        """

        if 0 <= indice_img < len(self.dic_imgs):
            return self.dic_imgs[indice_img]

        raise IndexError("La imagen consultada no existe")

    # ------------------------------------------------------------------------------------------------------------------

    def consultar_suj(self, indice_suj):

        """
        A partir de un índice que corresponda a un sujeto, se obtiene la ruta de la carpeta de dicho sujeto
        @param indice_suj: Índice devuelto por el clasificador
        @return: ruta_suj
        """

        if 0 <= indice_suj < len(self.dic_sujs):
            return self.dic_sujs[indice_suj]

        raise IndexError("El sujeto consultado no existe")

    # ------------------------------------------------------------------------------------------------------------------

    def obt_diccionarios(self):

        """
        Crea un diccionario con el siguiente formato: I : (S, R), donde I es el numero de imagen leida dentro de todas
        las presentes en la BD, S es el sujeto con el que se relaciona I, y R es la ruta de I. Esto se hace con el fin
        de eliminar la restricción de que cada sujeto deba tener exactamente 10 imagenes en su carpeta
        Además se obtiene el diccionario de sujetos con el formato I : R donde I es el índice del sujeto y R su ruta
        @return: no retorna ningun valor
        """

        # Obteniendo la carpeta de cada uno de los sujetos
        bd = os.path.join(Configuracion.RUTA_DATOS, Configuracion.REGEX_SUJS)
        ruta_sujs = glob.glob(bd)
        num_img = 0

        for i in range(0, len(ruta_sujs)):
            self.dic_sujs[i] = ruta_sujs[i]

            # Obteniendo imagenes (rutas) de cada sujeto en específico
            for img in glob.glob(ruta_sujs[i] + Configuracion.REGEX_IMGS):
                self.dic_imgs[num_img] = (ruta_sujs[i], img)
                num_img += 1

        if len(self.dic_sujs) == 0:
            raise Exception("No se ha encontrado ningún sujeto en la ruta especificada")

    # ------------------------------------------------------------------------------------------------------------------

    def obt_dimensiones(self):

        """
        Con base a la primera imagen indexada se infiere el tamaño de las demás imágenes dentro de la bd,
        esto porque se asume que todas las imágenes tienen las mismas dimensiones.
        @return: no retorna ningun valor
        """

        primer_clave = self.dic_imgs[0]
        ruta_img = primer_clave[1]
        img = cv.imread(ruta_img, 0)

        if img is None:
            raise IOError("Error al obtener las dimesiones de las imagenes de la colección")

        self.alto_img, self.ancho_img = img.shape

    # ------------------------------------------------------------------------------------------------------------------

    def obt_subconjunto(self, indices):

        """
        Obtiene una matriz de subconjunto a partir de la matriz de muestras
        @param indices: lista de los indices asociados a la columnas que se tomarán de la matriz de muestras
        @return: Tupla (M, I) donde M es la matriz subconjunto de la colección e I los indices utilizados
        """

        # Matriz vacia para colocar las imagenes
        dimension = (self.pixeles_img, len(indices))
        mat = np.empty(dimension, dtype='float64')

        col_actual = 0
        for i in indices:

            # Se abre la imagen en escala de grises
            img = cv.imread(self.consultar_img(i)[1], 0)

            # Si se logra abrir la imagen, esta se redimensiona,
            # vectoriza y se coloca como columna en el subconjunto
            if img is not None:
                img = img.reshape(self.alto_img, self.ancho_img)
                mat[:, col_actual] = np.array(img, dtype='float64').flatten()
                col_actual += 1

        return np.matrix(mat, dtype="float64")

    # ------------------------------------------------------------------------------------------------------------------

    def __str__(self):

        string = ""
        for num_img, tupla_suj_img in self.dic_imgs.items():
            suj = tupla_suj_img[0]
            img = tupla_suj_img[1]
            string += "\t".join([str(num_img), suj, img]) + "\n"

        return string

# ----------------------------------------------------------------------------------------------------------------------
