# ----------------------------------------------------------------------------------------------------------------------

import os

import pandas as pd


# ----------------------------------------------------------------------------------------------------------------------


class DaoEvaluacion(object):

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def guardar(evaluacion, directorio):

        """
        @author Julian Salinas, Andrey Mendoza, Armando Lopez, Brandon Dinarte
        @version 1.6.49
        Se crearán los archivos cvs a partir de las tablas generedas por la evaluación
        @param directorio: Ruta donde se guardarán las tablas generadas por la evaluacion
        @param evaluacion: objeto evaluacion con los valores calculados
        @return: no retorna ningun valor.
        """

        if not os.path.isdir(directorio):
            os.makedirs(directorio)

        tabla_evaluacion = evaluacion.agregar_encabezados_tabla_evaluaciones()
        tabla_evaluacion = pd.DataFrame(tabla_evaluacion)
        tabla_evaluacion.to_csv(os.path.join(directorio, "eval.inform.csv"), index=False, header=False)

        tabla_clasificaciones = evaluacion.agregar_encabezados_tabla_clasificaciones()
        tabla_evaluacion = pd.DataFrame(tabla_clasificaciones)
        tabla_evaluacion.to_csv(os.path.join(directorio, "eval.clasifs.csv"), index=False, header=False)

# ----------------------------------------------------------------------------------------------------------------------
