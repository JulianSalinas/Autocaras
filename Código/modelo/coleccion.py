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
        resolucion de cada una. Sirve para encontrar el sujeto con el que coincide una imagen al momente de clasificar
        @param ruta_datos: Ruta donde estan las imagenes
        @param regex_sujs: Expresión regula que indique que carpetas corresponden a sujetos
        @param regex_imgs: Expresión regula que indique archivos corresponden a la imagen de un sujeto
        """

        self.ruta_datos = ruta_datos
        self.regex_sujs = regex_sujs
        self.regex_imgs = regex_imgs

        self.dic_sujs, self.dic_imgs = self.obt_diccionarios()
        self.alto_img, self.ancho_img = self.obt_dimensiones()
        self.total_sujs = len(self.dic_sujs)
        self.total_imgs = len(self.dic_imgs)
        self.pixeles_img = self.ancho_img * self.alto_img
        self.mat_muestras = None

        self.ruta_suj_desconocido = os.path.join(self.ruta_datos, "otros")
        self.ruta_img_desconocida = os.path.join(self.ruta_suj_desconocido, "desconocido.pgm")

    # ------------------------------------------------------------------------------------------------------------------

    def consultar_img(self, indice_img):

        """
        Obtiene la ruta de la imagen según el índice obtenido de la matriz de imagenes de la colección
        @param indice_img: Índice devuelto por el clasificador
        @return: ruta_suj, ruta_img
        """

        if 0 <= indice_img < len(self.dic_imgs):
            return self.dic_imgs[indice_img]

        return self.ruta_suj_desconocido, self.ruta_img_desconocida

    # ------------------------------------------------------------------------------------------------------------------

    def consultar_suj(self, indice_suj):

        """
        A partir de un índice que corresponda a un sujeto, se obtiene la ruta de la carpeta de dicho sujeto
        @param indice_suj: Índice devuelto por el clasificador
        @return: ruta_suj
        """

        if 0 <= indice_suj < len(self.dic_sujs):
            return self.dic_sujs[indice_suj]

        return self.ruta_suj_desconocido

    # ------------------------------------------------------------------------------------------------------------------

    def obt_diccionarios(self):

        """
        Crea un diccionario con el siguiente formato: I : (S, R), donde I es el numero de imagen leida dentro de todas
        las presentes en la BD, S es el sujeto con el que se relaciona I, y R es la ruta de I. Esto se hace con el fin
        de eliminar la restricción de que cada sujeto deba tener exactamente 10 imagenes en su carpeta
        Además se obtiene el diccionario de sujetos con el formato I : R donde I es el índice del sujeto y R su ruta
        @return: Diccionario con el formato I : (S, R)
        """

        # Obteniendo la lista de las rutas de cada sujeto
        ruta_abs = os.path.join(self.ruta_datos, self.regex_sujs)
        ruta_sujs = glob.glob(ruta_abs)

        dic_sujs = {}
        dic_imgs = {}
        num_img = 0

        for i in range(0, len(ruta_sujs)):

            dic_sujs[i] = ruta_sujs[i]

            # Obteniendo imagenes (rutas) de cada sujeto en específico
            for img in glob.glob(ruta_sujs[i] + self.regex_imgs):
                dic_imgs[num_img] = (ruta_sujs[i], img)
                num_img += 1

        return dic_sujs, dic_imgs

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

            # Se abre la imagen en escala de grises y se recorta
            img = cv.imread(self.consultar_img(i)[1], 0)
            img = img.reshape(self.alto_img, self.ancho_img)

            # Se vectoriza la imagen, 2D a 1D y se coloca como columna
            mat[:, col_actual] = np.array(img, dtype='float64').flatten()

            col_actual += 1

        return np.matrix(mat, dtype="float64")

    # ------------------------------------------------------------------------------------------------------------------

    def indexar(self, sufijo):

        """
        Guarda en un archivo la informacion de la coleccion con el objetivo de ser utilizada a futuro.
        @param sufijo: sufijo a concantenar a cada archivo generado para poder identificarlos.
        @return: sin retorno
        """

        # Guardar informacion sobre el objeto coleccion
        f_coleccion = open('..\\..\\Index\\coleccion_' + sufijo + '.txt', 'w')
        coleccion = {'ruta_datos': self.ruta_datos,
                     'regex_sujs': self.regex_sujs,
                     'regex_imgs': self.regex_imgs,
                     'dic_sujs': self.dic_sujs,
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

