# ----------------------------------------------------------------------------------------------------------------------

from unittest import TestCase

from modelo.clasificador import *
from modelo.entrenamiento import *
from modelo.coleccion import *


# ----------------------------------------------------------------------------------------------------------------------

"""
@author Julian Salinas, Armando Lopez, Andrey Mendoza, Brandon Dinarte
@version 1.6.49
"""

class TestEntrenamientoClasificador(TestCase):

    # ------------------------------------------------------------------------------------------------------------------

    def test_entrenamiento_clasificador(self):

        """
        Entradas: El subconjunto utilizado por el entrenamiento, una coleccion con la que se consultaran los sujetos
        a partir de un indice obtenido usando el clasificador y un sujeto desconocido del cual se tenga certeza a que
        columna en la matriz se parece más.
        @param Sin parametros
        @return Sin retorno
        """

        # Configuramos una coleccion pequeña para verificar
        coleccion = Coleccion()
        coleccion.total_sujs = 3
        coleccion.total_imgs = 3

        # Matriz de muestras dada por la colección
        coleccion.obt_subconjunto = \
            lambda x: np.matrix([[30, 50, 40],
                                 [10, 9., 80],
                                 [78, 80, 76],
                                 [58, 24, 65]], "float64")

        # Diccionario de imagenes de la colección
        coleccion.dic_imgs = {0: ("suj0", "img1"), 1: ("suj1", "img1"), 2: ("suj2", "img1")}

        # Ejecutamos el entrenamiento
        entrenamiento = Entrenamiento(coleccion, porcentaje_coleccion=100, porcentaje_valores=100)

        # Creamos un sujeto desconocido de P x 1
        sujeto_desconocido = np.matrix([[40, 80],
                                        [76, 64.]])

        # Colocamos que la clasificación se realice con base al entrenamiento previo
        # y que el mínimo de aceptación sea 80 de lo contrario no se encontraría en el autoespacio
        clasificacion = Clasificador(entrenamiento, porcentaje_aceptacion=80)

        # Clasificamos el sujeto, esto nos debe dar el suj 2 pues es la columna que más
        # se parece al sujeto que creamos con anterioridad
        indice, similitud = clasificacion.clasificar(sujeto_desconocido)
        self.assertTrue(indice == 2)

# ----------------------------------------------------------------------------------------------------------------------
