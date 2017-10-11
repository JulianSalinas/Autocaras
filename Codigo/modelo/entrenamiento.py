# ----------------------------------------------------------------------------------------------------------------------

import numpy as np

# ----------------------------------------------------------------------------------------------------------------------


class Entrenamiento(object):

    def __init__(self, coleccion, porcentaje_coleccion, porcentaje_valores):

        """
        Clase encargada de realizar el entrenamiento del sistema. El resultado de objetivo de este entrenamiento es
        encontrar los autovectores/caras que componen el autoespacio, además de sus respectivas proyecciones (o pesos)
        Además se guarda la muestra promedio para centrar las imagenes al origen cuando sea necesario clasificarlas
        @param coleccion: Instancia de Coleccion de donde vamos a extraer las imagenes
        @param porcentaje_coleccion: Representa la cant de imagenes que usaremos de la coleccion
        @param porcentaje_valores: Número que determine la cantidad de valores (o componentes) que se desean conservar
        """

        # Obtenemos los índices de la coleccion de las imagenes que usaremos de muestra
        self.indices_entrenamiento = None
        self.obt_indices_entrenamiento(coleccion, porcentaje_coleccion)

        # Obtenemos la matriz de muestras para realizar el entrenamiento
        mat_entrenamiento = coleccion.obt_subconjunto(self.indices_entrenamiento)

        # Se centran todas las muestras de Px1 de la matriz A (PxM) al origen
        self.muestra_promedio = np.mean(mat_entrenamiento, axis=1, dtype="float64")
        mat_entrenamiento -= self.muestra_promedio

        # Se obtiene la matriz de covarianza C (MxM para ahorrar costo computacional)
        mat_covarianza = mat_entrenamiento.T * mat_entrenamiento
        mat_covarianza /= mat_entrenamiento.shape[1] - 1

        # Para C se obtienen los autovectores V.
        autovals, autovects = np.linalg.eig(mat_covarianza)

        # Ordenar y obtener las autocaras mas significantes
        cant_valores = int(mat_entrenamiento.shape[1] * porcentaje_valores / 100)
        orden = np.argsort(autovals)[::-1]
        autovects = autovects[orden]
        autovects = autovects[0: cant_valores]

        # Se ocupan los autovectores U de la matriz PxP, por lo que se usa la fórmula U = AxV
        self.autoespacio = mat_entrenamiento * autovects.T
        self.autoespacio /= np.linalg.norm(self.autoespacio, axis=0)

        # Se realiza las proyecciones al nuevo autoespacio
        self.proyecciones = self.autoespacio.T * mat_entrenamiento

# ----------------------------------------------------------------------------------------------------------------------

    def obt_indices_entrenamiento(self, coleccion, porcentaje_coleccion):

        """
        Obtenemos los índices de la coleccion de las imagenes que vamos a utilizar para el entrenamiento
        @param coleccion: Instancia de Coleccion de donde vamos a extraer las imagenes
        @param porcentaje_coleccion: Representa la cant de imagenes que usaremos de la coleccion
        @return: no retorna ningun valor
        """

        self.indices_entrenamiento = np.array([], dtype="int32")

        total_sujs = coleccion.total_sujs
        imgs_x_suj = coleccion.total_imgs // total_sujs
        cant_imgs = int(imgs_x_suj * porcentaje_coleccion / 100)

        for i in range(0, total_sujs):
            escogidos = np.random.choice(range(0, imgs_x_suj), cant_imgs, False)
            escogidos += i * imgs_x_suj
            escogidos = np.sort(escogidos)
            self.indices_entrenamiento = np.append(self.indices_entrenamiento, [escogidos])

# ----------------------------------------------------------------------------------------------------------------------

