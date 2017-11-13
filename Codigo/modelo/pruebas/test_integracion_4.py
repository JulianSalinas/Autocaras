# ----------------------------------------------------------------------------------------------------------------------

import subprocess
from unittest import TestCase

from controlador.dao_evaluacion import *
from modelo.clasificador import *
from modelo.entrenamiento import *
from modelo.evaluacion import *


# ----------------------------------------------------------------------------------------------------------------------

"""
@author Julian Salinas, Armando Lopez, Andrey Mendoza, Brandon Dinarte
@version 1.6.49
"""

class TestIntegracion4(TestCase):
    """
    Prueba encargada de probar la integracion entre la evalucion y el DAOEvaluacion
    Esto se logra por medio de un assert para verificar que la se haya creado o que existe
    """

    # ------------------------------------------------------------------------------------------------------------------

    def test_integracion4(self):

        """
        Entradas: Entrenamiento previo del sistema, nombre del directorio donde se guardarán los informes generados
        por la evaluacion del sistema
        Resultado esperado: Dos archivos csv no vacios
        @param Sin parametros
        @return Sin retorno
        """

        # Colocamos la configuracion para que la coleccion solo se tenga 4 sujetos
        Configuracion.REGEX_SUJS = "s[1-4]"
        coleccion = Coleccion()

        # Se usará un 50% de la colección (al azar) para evaluar el sistema. Se usará el 80% de autocaras
        entrenamiento = Entrenamiento(coleccion, porcentaje_coleccion=50, porcentaje_valores=80)

        # Ejecutamos la evaluación usando el entrenamiento previo. Se usa un indice de aceptacion de 0. para que todos
        # los rostros sean considerados como que se encuentran dentro del autoespacio, es decir, aunque la entrada sea
        # una imagen que no sea un rostro, de igual manera se tomará la más cercana
        evaluacion = Evaluacion(coleccion, entrenamiento, Clasificador(entrenamiento, 0))

        # Se guardan las tablas generadas por la evaluación como archivos csv
        DaoEvaluacion.guardar(evaluacion, Configuracion.RUTA_EVALUACION)

        # Se comprueba que la carpeta se haya creado (o que exista)
        self.assertTrue(os.path.isdir(Configuracion.RUTA_EVALUACION))
        self.assertTrue(os.path.exists(Configuracion.RUTA_EVALUACION))

        # Verificamos manualmente que los archivos existan y que no esten vacio viendo la carpeta
        subprocess.call("explorer " + os.path.join(Configuracion.RUTA_MEDIA), shell=True)

# ----------------------------------------------------------------------------------------------------------------------

