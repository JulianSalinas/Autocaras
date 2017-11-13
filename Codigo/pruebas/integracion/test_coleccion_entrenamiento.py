# ----------------------------------------------------------------------------------------------------------------------

from unittest import TestCase

from modelo.clasificador import *
from modelo.entrenamiento import *


# ----------------------------------------------------------------------------------------------------------------------

"""
@author Julian Salinas, Armando Lopez, Andrey Mendoza, Brandon Dinarte
@version 1.6.49
"""

class TestColeccionEntrenamiento(TestCase):

    # ------------------------------------------------------------------------------------------------------------------

    def test_coleccion_entrenamiento(self):

        """
        Integración de la clase colección con la clase entrenamiento. Se prueba que las funciones de la clase coleccion
        puedan ser usadas en el entrenamiento.
        Entradas:
            Configuración de la coleccion, porcentaje de la coleccion.
        Salidas:
            Se espera que de la coleccion se obtenga la cantidad correcta de imagenes según se especifique como
            parámetro del entrenamiento. Además, se espera que los resultados del entrenamiento tengan las dimensiones
            correctas.
        """

        # Colocamos la configuracion para que solo se lean 4 imagenes de los primeros 4 sujetos
        Configuracion.RUTA_DATOS = "..\\..\\datos"
        Configuracion.REGEX_SUJS = "s[1-4]"
        Configuracion.REGEX_IMGS = "\\[1-4].pgm"

        coleccion = Coleccion()
        entrenamiento = Entrenamiento(coleccion, porcentaje_coleccion=50, porcentaje_valores=100)

        # Si la coleccion contiene 4 sujetos y 4 imagenes por cada uno, si se usa el 50 porciento de la colección
        # entonces el entrenamiento debería de usar 8 imagenes
        self.assertTrue(len(entrenamiento.indices_entrenamiento), 8)

        # Se prueba que el autoespacio generado tenga dimensiones 10304x8, es decir, la cantidad pixeles de una imagen
        # por la cantidad de imagenes que se usaron en el entrenamiento
        self.assertTrue(entrenamiento.autoespacio.shape, (10304, 8))

        # La muestra promedio debe contener la cantidad de pixeles
        self.assertTrue(entrenamiento.muestra_promedio.shape, (10304, 1))

        # Las proyecciones tienen que ser una matriz de 8x8
        self.assertTrue(entrenamiento.proyecciones.shape, (8, 8))


# ----------------------------------------------------------------------------------------------------------------------

