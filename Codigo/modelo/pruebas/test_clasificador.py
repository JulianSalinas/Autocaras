# ----------------------------------------------------------------------------------------------------------------------

from unittest import TestCase
from modelo.entrenamiento import *
from modelo.clasificador import *

# ----------------------------------------------------------------------------------------------------------------------


class TestClasificacion(TestCase):

    # ------------------------------------------------------------------------------------------------------------------

    def test_clasificar(self):

        def obt_subconjunto(args):
            return np.matrix([[30, 50, 40],
                              [10, 9., 80],
                              [78, 80, 76],
                              [58, 24, 65]], "float64")

        # Configuramos una coleccion pequeña para verificar
        coleccion = Coleccion()
        coleccion.total_sujs = 3
        coleccion.total_imgs = 3
        coleccion.obt_subconjunto = obt_subconjunto
        coleccion.dic_imgs = {0: ("suj0", "img1"), 1: ("suj1", "img1"), 2: ("suj2", "img1")}

        # Ejecutamos el entrenamiento
        entrenamiento = Entrenamiento(coleccion, porcentaje_coleccion=100, porcentaje_valores=70)

        # Creamos un sujeto desconocido de P x 1
        sujeto_desconocido = np.matrix([[40, 80],
                                        [76, 64.]])

        # Colocamos que la clasificación se realice con base al entrenamiento previo
        # y que el mínimo de aceptación sea 80 de lo contrario no se encuentra en el autoespacio
        clasificacion = Clasificador(entrenamiento, porcentaje_aceptacion=80)

        # Clasificamos el sujeto, esto nos debe dar el suj 2 pues es la columna que más
        # se parece al sujeto
        indice, similitud = clasificacion.clasificar(sujeto_desconocido)
        self.assertTrue(indice == 2)


# ----------------------------------------------------------------------------------------------------------------------

