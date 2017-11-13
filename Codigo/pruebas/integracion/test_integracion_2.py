# ----------------------------------------------------------------------------------------------------------------------

from unittest import TestCase

from modelo.coleccion import *


# ----------------------------------------------------------------------------------------------------------------------

"""
@author Julian Salinas, Armando Lopez, Andrey Mendoza, Brandon Dinarte
@version 1.6.49
"""

class TestColeccion(TestCase):

    # ------------------------------------------------------------------------------------------------------------------

    def test_coleccion(self):

        """
        Entradas: Configuración de la colección
        Resultado esperado: Las propiedades de la colección deben coincidir con las que se saben de antemano,
        debe coincidir el # de sujetos, el de imagenes y las dimesiones de cada una
        @param Sin parametros
        @return Sin retorno
        """

        # Colocamos la configuracion para que solo se lean 3 imagenes de los primeros 2 sujetos
        Configuracion.RUTA_DATOS = "..\\..\\datos"
        Configuracion.REGEX_SUJS = "s[1-2]"
        Configuracion.REGEX_IMGS = "\\[1-3].pgm"

        # Instanciamos la colección, es decir, los diccionarios con las imagenes
        coleccion = Coleccion()

        # Se sabe que hay dos sujetos
        self.assertEqual(coleccion.total_sujs, 2)

        # Se sabe que entre esos 2 sujetos existen 6 imagenes
        self.assertEqual(coleccion.total_imgs, 6)

        # Tambien se sabe que cada imagen de la BD mide 112 de alto y 92 de ancho
        self.assertEqual((coleccion.alto_img, coleccion.ancho_img), (112, 92))

        # Por tanto, la cantidad de pixeles de la imagen es 10304
        self.assertEqual(coleccion.pixeles_img, 10304)

        print("\nColección de imagenes I : (S, R) :")
        print(str(coleccion))

# ----------------------------------------------------------------------------------------------------------------------
