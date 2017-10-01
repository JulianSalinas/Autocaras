# ----------------------------------------------------------------------------------------------------------------------

import os
import glob
import cv2 as cv
import numpy as np

# ----------------------------------------------------------------------------------------------------------------------


class Coleccion(object):

    def __init__(self, ruta_datos, regex_sujs, regex_imgs):

        """
        Encargada de proporcionar las rutas de cada una de las imagenes presentes en la base de datos, asi como otra
        información importante, como la cantidad de sujetos, la cantidad de imagenes totales y por sujeto junto con la
        resolucion de cada una. Sirve para encontrar el sujeto con el que coincide una imagen al momente de clasificar.
        @param ruta_datos: Ruta donde estan las imagenes.
        @param regex_sujs: Expresión regula que indique que carpetas corresponden a sujetos.
        @param regex_imgs: Expresión regula que indique archivos corresponden a la imagen de un sujeto.
        """

        self.ruta_datos = ruta_datos
        self.regex_sujs = regex_sujs
        self.regex_imgs = regex_imgs

        self.dic_imgs = self.obt_diccionario()
        self.alto_img, self.ancho_img = self.obt_dimensiones()
        self.total_imgs = len(self.dic_imgs)
        self.pixeles_img = self.ancho_img * self.alto_img

    # ------------------------------------------------------------------------------------------------------------------

    def consultar(self, indice_img):

        """
        A partir de un índice que corresponda a una columna de la matriz de imagenes de muestra, se busca en el
        diccionario de imagenes dicho índice.
        @param indice_img: Índice devuelto por el clasificador
        @return: Tupla (S, R) donde S es la ruta de la carpeta del sujeto y R una de sus imagenes.
        """

        return self.dic_imgs[indice_img]

    # ------------------------------------------------------------------------------------------------------------------

    def obt_diccionario(self):

        """
        Crea un diccionario con el siguiente formato: I : (S, R), donde I es el numero de imagen leida dentro de todas
        las presentes en la BD, S es el sujeto con el que se relaciona I, y R es la ruta de I. Esto se hace con el fin
        de eliminar la restricción de que cada sujeto deba tener exactamente 10 imagenes en su carpeta.
        @return: Diccionario con el formato I : (S, R).
        """

        # Obteniendo la lista de las rutas de cada sujeto
        ruta_abs = os.path.join(self.ruta_datos, self.regex_sujs)
        ruta_sujs = glob.glob(ruta_abs)

        dic_imgs = {}
        num_img = 0
        for suj in ruta_sujs:

            # Obteniendo imagenes (rutas) de cada sujeto en específico
            for img in glob.glob(suj + self.regex_imgs):
                dic_imgs[num_img] = (suj, img)
                num_img += 1

        return dic_imgs

    # ------------------------------------------------------------------------------------------------------------------

    def obt_dimensiones(self):

        """
        Con base a la primera imagen indexada se infiere el tamaño de las demás imágenes dentro de la bd, esto porque
        se asume que todas las imágenes tienen las mismas dimensiones.
        @return: Tupla (N, M), donde N es el ancho y M el alto de la imagen.
        """

        primer_clave = self.dic_imgs[0]
        primer_img = primer_clave[1]
        return cv.imread(primer_img, 0).shape

    # ------------------------------------------------------------------------------------------------------------------

    def obt_matriz_muestras(self):

        """
        Lee, recorta, vectoriza y coloca cada una de las imagenes como un vector columna a la matriz de muestras.
        @return: Matriz de muestras donde cada columna representa una imagen a escala de grises.
        """

        # Matriz vacia para colocar las imagenes
        dimension = (self.pixeles_img, self.total_imgs)
        mat = np.empty(dimension, dtype='float64')

        col_actual = 0
        for ruta_img in self.dic_imgs.values():

            # Se abre la imagen en escala de grises y se recorta
            img = cv.imread(ruta_img[1], 0)
            img = img.reshape(self.alto_img, self.ancho_img)

            # Se vectoriza la imagen, 2D a 1D y se coloca como columna
            mat[:, col_actual] = np.array(img, dtype='float64').flatten()

            col_actual += 1

        return np.matrix(mat, dtype="float64")

    # ------------------------------------------------------------------------------------------------------------------

    def indexar(self, sufijo):

        """
        Guarda en un archivo la informacion de la coleccion con el objetivo de ser utilizada a futuro.
        :param sufijo: sufijo a concantenar a cada archivo generado para poder identificarlos.
        :return: sin retorno
        """

        # Guardar informacion sobre el objeto coleccion
        f_coleccion = open('..\\..\\Index\\coleccion_' + sufijo + '.txt', 'w')
        coleccion = {'ruta_datos': self.ruta_datos,
                     'regex_sujs': self.regex_sujs,
                     'regex_imgs': self.regex_imgs,
                     'dic_imgs': self.dic_imgs,
                     'alto_imgs': self.alto_img,
                     'ancho_imgs': self.ancho_img,
                     'total_imgs': self.total_imgs,
                     'pixeles_img': self.pixeles_img}
        f_coleccion.write(str(coleccion))
        f_coleccion.close()

# ----------------------------------------------------------------------------------------------------------------------

    def __str__(self):

        string = ""
        for num_img, tupla_suj_img in self.dic_imgs.items():
            suj = tupla_suj_img[0]
            img = tupla_suj_img[1]
            string += "\t".join([str(num_img), suj, img]) + "\n"

        return string

# ----------------------------------------------------------------------------------------------------------------------

