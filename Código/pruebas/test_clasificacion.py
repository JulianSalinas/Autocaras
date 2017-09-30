# ----------------------------------------------------------------------------------------------------------------------

import time
from unittest import TestCase

from Código.modelo.entrenamiento import *
from Código.modelo.clasificacion import *
from Código.pruebas.imprimir import *


# ----------------------------------------------------------------------------------------------------------------------


class TestClasificacion(TestCase):

    def setUp(self):
        imprimir_azul("\n-------------------------------------------------------------------------------------------\n")

    # ------------------------------------------------------------------------------------------------------------------

    def test_ejecutar(self):

        imprimir_verde("Test de 'Clasificacion.ejecutar' iniciado")
        inicio = time.time()

        # Creamos una matriz de muestras ficticia y verificable
        mat_muestras = np.matrix([[30, 50, 40],
                                  [10, 9., 80],
                                  [78, 80, 76],
                                  [58, 24, 65]], "float64")

        # Entrenamos el sistema con dicha matriz
        entrenamiento = Entrenamiento().ejecutar(mat_muestras, cant_valores=2)

        # Creamos un sujeto desconocido de P x 1
        sujeto_desconocido = np.matrix([[40, 80],
                                        [76, 64.]])

        # Colocamos que la clasificación se realice con base al entrenamiento previo
        # y que mínimo de aceptación es 50 de lo contrario no se encuentra en el autoespacio
        clasificacion = Clasificacion(entrenamiento, 50)

        # Clasificamos el sujeto, esto nos debe dar el índice 2 pues es la columna que más
        # se parece al sujeto
        indice, aceptacion = clasificacion.ejecutar(sujeto_desconocido)
        self.assertTrue(aceptacion != -1)
        self.assertTrue(indice == 2)

        print("Aceptación = " + str(aceptacion))

        fin = time.time() - inicio
        imprimir_verde("Test de 'Clasificacion.ejecutar' finalizado en " + str(fin) + " segundos")


# ----------------------------------------------------------------------------------------------------------------------

