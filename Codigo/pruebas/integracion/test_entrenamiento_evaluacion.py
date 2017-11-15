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

class TestEntrenamientoEvaluacion(TestCase):

    """
    Prueba encargada de verificar la integracion entre el entrenamiento y la evaluacion
    Esto se logra por medio del assert de las tablas que se guardan en la evaluacion y las dimensiones que estas adquieren

    Dimensiones esperadas en las tablas de la evaluacion:
        tabla_evaluacion        -> 4 x 5:
            Donde cada fila corresponde a un sujeto y cada columna contiene los vp, fp, fn, recall, precision

        tabla_clasificaciones   -> 4 x 4:
            Donde la cada fila corresponde al sujeto clasificado y las columnas a los reales
    """

    # ------------------------------------------------------------------------------------------------------------------

    def test_entrenamiento_evaluacion(self):

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

        # Tabla donde cada fila corresponde a un sujeto y cada columna
        # contiene los vp, fp, fn, recall, precision
        print("Tabla de evaluacion \n" + str(evaluacion.tabla_evaluacion))
        self.assertTrue(evaluacion.tabla_evaluacion.shape, (4,5))

        # Tabla de sujetos clasificadas vs reales
        """
        Se obtiene la tabla de sujetos clasificados vs los sujetos reales.
        Donde la cada fila corresponde al sujeto clasificado y las columnas a los reales
        Tiene el siguiente formato:
                                suj_real1   suj_real2   suj_realN
            suj_clasificado1        int         int         int
            suj_clasificado2        int         int         int
            suj_clasificadoN        int         int         int        
        """

        print("Tabla de clasificaciones \n" + str(evaluacion.tabla_clasificaciones))
        self.assertTrue(evaluacion.tabla_clasificaciones.shape, (4, 4))


# ----------------------------------------------------------------------------------------------------------------------

