# ----------------------------------------------------------------------------------------------------------------------

import time
from unittest import TestCase

from Código.modelo.coleccion import *
from Código.pruebas.imprimir import *


# ----------------------------------------------------------------------------------------------------------------------


class TestColeccion(TestCase):

    # ------------------------------------------------------------------------------------------------------------------

    def test_indexar(self):

        imprimir_verde("Test de 'indexar' iniciado")
        inicio = time.time()

        # Solo leerá las primeras 3 imagenes de los primeros 2 sujetos
        coleccion = Coleccion(ruta_datos='..\\..\\Datos', regex_sujs='s[1-2]', regex_imgs="\\[1-3].pgm")

        duracion = time.time() - inicio
        imprimir_verde("Duración de 'indexar': " + str(duracion))

        # Se sabe que entre esos 2 sujetos existen 6 imagenes
        self.assertEqual(coleccion.total_imgs, 6)

        # Tambien se sabe que cada imagen de la BD mide 112 de alto y 92 de ancho
        self.assertEqual((coleccion.alto_img, coleccion.ancho_img), (112, 92))

        # Por tanto, la cantidad de pixeles de la imagen es 10304
        self.assertEqual(coleccion.pixeles_img, 10304)

        imprimir_morado("\nColección de imagenes I : (S, R) :")
        print(str(coleccion))

        fin = time.time() - inicio
        imprimir_verde("Test de 'indexar' finalizado en " + str(fin) + " segundos")

    # ------------------------------------------------------------------------------------------------------------------

    def test_obt_matriz_muestras(self):

        imprimir_verde("Test de 'obt_mat_muestras' iniciado")
        inicio = time.time()

        # Solo leera las imagenes del primer sujeto
        coleccion = Coleccion(ruta_datos='..\\..\\Datos', regex_sujs='s1', regex_imgs="\*")

        # Se invoca el método a probar
        mat_muestras = coleccion.obt_matriz_muestras()

        duracion = time.time() - inicio
        imprimir_verde("Duración de 'obt_mat_muestras': " + str(duracion))

        # La cantidad de filas de la matriz de muestra debe ser igual a la cantidad de pixeles de una de sus imgs
        self.assertEqual(mat_muestras.shape[0], 10304)

        # La cantidad de columnas de la matriz debe ser igual a la cantidad de imagenes leidas del 1er sujeto
        self.assertEqual(mat_muestras.shape[1], 10)

        # Todos los pixeles de cada imagen deben estar entre 0 y 255
        self.assertTrue((mat_muestras <= 255).all())
        self.assertTrue((mat_muestras >= 0).all())

        imprimir_morado("\nMatriz de muestras")
        print(str(mat_muestras) + "\n")

        fin = time.time() - inicio
        imprimir_verde("Test de 'obt_mat_muestras' finalizado en " + str(fin) + " segundos")

# ----------------------------------------------------------------------------------------------------------------------
