# ----------------------------------------------------------------------------------------------------------------------

import time
from unittest import TestCase

from clasificador import *
from imprimir import *


# ----------------------------------------------------------------------------------------------------------------------


class TestClasificacion(TestCase):

    # ------------------------------------------------------------------------------------------------------------------

    def test_clasificar(self):

        imprimir_verde("Test de 'clasificar' iniciado")
        inicio = time.time()

        # Creamos una matriz de muestras ficticia y verificable
        mat_muestras = np.matrix([[30, 50, 40],
                                  [10, 9., 80],
                                  [78, 80, 76],
                                  [58, 24, 65]], "float64")

        # Entrenamos el sistema con dicha matriz
        entrenamiento = Entrenamiento(mat_muestras, porcentaje_valores=70)

        # Creamos un sujeto desconocido de P x 1
        sujeto_desconocido = np.matrix([[40, 80],
                                        [76, 64.]])

        # Colocamos que la clasificación se realice con base al entrenamiento previo
        # y que el mínimo de aceptación sea 80 de lo contrario no se encuentra en el autoespacio
        clasificacion = Clasificador(entrenamiento, porcentaje_aceptacion=80)

        # Clasificamos el sujeto, esto nos debe dar el índice 2 pues es la columna que más
        # se parece al sujeto
        indice, aceptacion = clasificacion.clasificar(sujeto_desconocido)
        self.assertTrue(indice == 2)

        print("Aceptación = " + str(aceptacion))

        fin = time.time() - inicio
        imprimir_verde("Test de 'clasicar' finalizado en " + str(fin) + " segundos")


# ----------------------------------------------------------------------------------------------------------------------

