# ----------------------------------------------------------------------------------------------------------------------

import numpy as np

# ----------------------------------------------------------------------------------------------------------------------


class Entrenamiento(object):

    def __init__(self, mat_muestras, indice_valores):

        """
        Clase encargada de realizar el entrenamiento del sistema. El resultado de objetivo de este entrenamiento es
        encontrar los autovectores/caras que componen el autoespacio, además de sus respectivas proyecciones (o pesos).
        Además se guarda la muestra promedio para centrar las imagenes al origen cuando sea necesario clasificarlas.
        @param mat_muestras: Matriz PxM, P es la cantidad de pixeles y M la de imágenes
        @param indice_valores: Índice [0,1] que determine la cantidad de valores (o componentes) que se desean conservar
        """

        # Se centran todas las muestras de Px1 de la matriz A (PxM) al origen.
        self.muestra_promedio = np.mean(mat_muestras, axis=1, dtype="float64")
        mat_muestras -= self.muestra_promedio

        # Se obtiene la matriz de covarianza C (MxM para ahorrar costo computacional).
        mat_covarianza = mat_muestras.T * mat_muestras
        mat_covarianza /= mat_muestras.shape[1] - 1

        # Para C se obtienen los autovectores V.
        autovals, autovects = np.linalg.eig(mat_covarianza)

        # Ordenar y obtener las autocaras mas significantes
        cant_valores = int(mat_muestras.shape[1] * indice_valores)
        orden = np.argsort(autovals)[::-1]
        autovects = autovects[orden]
        autovects = autovects[0: cant_valores]

        # Se ocupan los autovectores U de la matriz PxP, por lo que se usa la fórmula U = AxV.
        self.autoespacio = mat_muestras * autovects.T
        self.autoespacio /= np.linalg.norm(self.autoespacio, axis=0)

        # Se realiza las proyecciones al nuevo autoespacio.
        self.proyecciones = self.autoespacio.T * mat_muestras

# ----------------------------------------------------------------------------------------------------------------------

    def indexar(self, sufijo):

        """
        Guardar la información del entrenamiento realizado con el objetivo de realizar busquedas sobre esta informacion
        sin necesidad de volver a ser calculada.
        :param sufijo: sufijo a concatenar a cada uno de los archivos generados para poder identificarlos
        :return: sin retorno
        """

        sufijo += '.txt'
        prefijo = '..\\..\\Index\\'

        np.savetxt(prefijo + 'muestra_promedio_' + sufijo, self.muestra_promedio)
        np.savetxt(prefijo + 'autoespacio_' + sufijo, self.muestra_promedio)
        np.savetxt(prefijo + 'proyecciones_' + sufijo, self.muestra_promedio)


# ----------------------------------------------------------------------------------------------------------------------
