# ----------------------------------------------------------------------------------------------------------------------

from unittest import TestCase
from modelo.coleccion import *


# ----------------------------------------------------------------------------------------------------------------------


class TestColeccion(TestCase):

    # ------------------------------------------------------------------------------------------------------------------

    def test_coleccion(self):

        # Colocamos la configuracion para que solo se lean 3 imagenes de los primeros 2 sujetos
        Config.RUTA_DATOS = "..\\..\\datos"
        Config.REGEX_SUJS = "s[1-2]"
        Config.REGEX_IMGS = "\\[1-3].pgm"

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

    # ------------------------------------------------------------------------------------------------------------------

    def test_obt_subconjunto(self):

        # Colocamos la informacion para que solo lea las imagenes del primers sujeto
        Config.RUTA_DATOS = "..\\..\\datos"
        Config.REGEX_SUJS = "s1"
        Config.REGEX_IMGS = "\*"

        # Solo indexara las imagenes del primer sujeto
        coleccion = Coleccion()

        # De las 10 imagenes del sujeto, se tomarán solo 3 (la 1, 3 y 4)
        mat_muestras = coleccion.obt_subconjunto([1, 3, 4])

        # La cantidad de filas de la matriz de muestra debe ser igual a la cantidad de pixeles de una de sus imgs
        self.assertEqual(mat_muestras.shape[0], 10304)

        # La cantidad de columnas de la matriz debe ser igual a la cantidad de imagenes leidas (que son 3)
        self.assertEqual(mat_muestras.shape[1], 3)

        # Todos los pixeles de cada imagen deben estar entre 0 y 255
        self.assertTrue((mat_muestras <= 255).all())
        self.assertTrue((mat_muestras >= 0).all())

# ----------------------------------------------------------------------------------------------------------------------
