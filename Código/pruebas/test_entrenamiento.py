# ----------------------------------------------------------------------------------------------------------------------

import time
from unittest import TestCase

from Código.pruebas.imprimir import *


# ----------------------------------------------------------------------------------------------------------------------


class TestEntrenamiento(TestCase):

    # ------------------------------------------------------------------------------------------------------------------

    def test_entrenamiento(self):

        imprimir_verde("Test de 'entrenamiento' iniciado")
        inicio = time.time()

        # Creamos una matriz de muestras ficticia y verificable
        mat_muestras = np.matrix([[30, 50, 40],
                                  [10, 9., 80],
                                  [78, 80, 76],
                                  [58, 24, 65]], "float64")

        # Entrenamos con la cantidad de valores que queremos conservar para el análisis
        # Emulando la ejecución de 'Entrenamiento(mat_muestras, porcentaje_valores=85)'

        # Comprobando matriz de muestras con base al origen
        # Si la imagen esta centrada con base al origen, su sumatoria es 0
        self.muestra_promedio = np.mean(mat_muestras, axis=1, dtype="float64")
        mat_muestras -= self.muestra_promedio
        self.assertEqual(np.sum(mat_muestras), 0)

    # ------------------------------------------------------------------------------------------------------------------

        # Comprobando matriz de covarianza (sin no normalizar)
        mat_covarianza = mat_muestras.T * mat_muestras

        # Se comprueba que sea cuadrada
        self.assertEqual(mat_covarianza.shape[0], mat_covarianza.shape[1])

        # Se comprueba que cada valor de la matriz sea igual al de la obtenida en manualmente
        mat_covarianza_real = np.matrix([[710.,  227.,  -937.],
                                         [227.,  1305., -1532],
                                         [-937, -1532., 2469.]], "float64")
        self.assertTrue((mat_covarianza == mat_covarianza_real).all())

    # ------------------------------------------------------------------------------------------------------------------

        # Para C se obtienen los autovectores V.
        autovals, autovects = np.linalg.eig(mat_covarianza)
        autovects = autovects.T

        # Comprobando contra los resultados obtenidos en
        # http: // www.arndt - bruenner.de / mathe / scripts / engl_eigenwert2.htm
        autovals_reales = np.array([3.79167771e+03, 6.92322292e+02, -1.89631347e-13], "float64")
        autovects_reales = np.matrix([[-0.28312967, -0.5216683, 0.80479797],
                                     [-0.76583566, 0.62811532, 0.13772034],
                                     [0.57735027,  0.57735027, 0.57735027]], "float64")
        self.assertTrue(np.allclose(autovals, autovals_reales))
        self.assertTrue(np.allclose(autovects, autovects_reales))

    # ------------------------------------------------------------------------------------------------------------------

        # Se ordenan los autovectores con base a los autovalores, se conservan solo los requeridos (2)
        # Se comprueba que los autovectores con autovalores mas altos sean los que se conservan
        autovects = autovects[np.argsort(autovals)[::-1]]
        autovects = autovects[0:2]
        autovects_reales = np.matrix([[-0.28312967, -0.5216683, 0.80479797],
                                      [-0.76583566, 0.62811532, 0.13772034]], "float64")
        self.assertTrue(np.allclose(autovects, autovects_reales))

    # ------------------------------------------------------------------------------------------------------------------

        # Se ocupan los autovectores U de la matriz PxP, por lo que se usa la fórmula U = AxV.
        autoespacio = mat_muestras * autovects.T
        autoespacio /= np.linalg.norm(autoespacio, axis=0)
        autoespacio_real = np.matrix([[-0.03873852, 0.5297773],
                                      [0.92336254,  0.34251681],
                                      [-0.04308345, 0.03727536],
                                      [0.37953229, -0.77500245]], "float64")
        self.assertTrue(np.allclose(autoespacio, autoespacio_real))

    # ------------------------------------------------------------------------------------------------------------------

        # Finalmente, se realiza las proyecciones al nuevo autoespacio.
        proyecciones = autoespacio.T * mat_muestras
        proyecciones_reales = np.matrix([[-17.43416274, -32.1225603, 49.55672304],
                                         [-20.15068162, 16.52698157, 3.62370005]], "float64")
        self.assertTrue(np.allclose(proyecciones, proyecciones_reales))

    # ------------------------------------------------------------------------------------------------------------------

        fin = time.time() - inicio
        imprimir_verde("Test de 'entrenamiento' finalizado en " + str(fin) + " segundos")


# ----------------------------------------------------------------------------------------------------------------------

