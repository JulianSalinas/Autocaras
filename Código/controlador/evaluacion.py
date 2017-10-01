# ----------------------------------------------------------------------------------------------------------------------

from clasificacion import *
from entrenamiento import *
from coleccion import *

# ----------------------------------------------------------------------------------------------------------------------


class Evaluacion(object):

    def __init__(self, coleccion, indice_evaluacion, indice_valores, indice_aceptacion):

        """
        Clase usada para evaluar la precisión y exhaustividad  del sistema. Se toma un porcentaje de imagenes de la
        colección para entrenar el sistema y otro porcentaje para clasificar (escogidas aleatoriamente respetando
        la cantidad que se deben tomar).
        @param coleccion: coleccion indexada con toda las imagenes de la BD
        @param indice_evaluacion: Índice que indica cuantas de las imagenes serán usadas clasificar
        @param indice_valores: Índice [0,1] que determine la cantidad de valores (o componentes) que se desean conservar
        @param indice_aceptacion: Índice para decidir si la imagen es lo suficientemente parecida a una de las img
        """

        # Obtenemos la matriz de muestras para toda la colección
        self.coleccion = coleccion
        self.total_sujs = coleccion.total_sujs
        self.mat_muestras = coleccion.obt_matriz_muestras()

        # Con base a la colección obtenemos las claves de las imagenes para evaluar y las que son para entrenar
        self.indices_imgs_evaluacion = self.obt_indices_imgs_evaluacion(indice_evaluacion)
        self.indices_imgs_entrenamiento = np.delete(range(0, coleccion.total_imgs), self.indices_imgs_evaluacion)

        # Matrices donde cada columna es una imagen para evaluar y para entrenar respectivamente
        self.mat_evaluacion = self.mat_muestras[:, self.indices_imgs_evaluacion]
        self.mat_entrenamiento = self.mat_muestras[:, self.indices_imgs_entrenamiento]

        tabla_clasificado_vs_real = self.obt_clasificado_vs_real(indice_valores, indice_aceptacion)
        self.tabla_evaluacion = self.obt_tabla_evaluacion(tabla_clasificado_vs_real)

    # ------------------------------------------------------------------------------------------------------------------

    def obt_indices_imgs_evaluacion(self, indice_evaluacion):

        cant_imgs_evaluacion = int(10 * indice_evaluacion)
        indices_imgs_evaluacion = np.array([], dtype="int32")
        for i in range(0, self.total_sujs):
            escogidos = np.random.choice(range(0, 10), cant_imgs_evaluacion, False) + (i * 10)
            escogidos.sort()
            indices_imgs_evaluacion = np.append(indices_imgs_evaluacion, [escogidos])

        return indices_imgs_evaluacion

    # ------------------------------------------------------------------------------------------------------------------

    def obt_clasificado_vs_real(self, indice_valores, indice_aceptacion):

        # Entrenamos el sistema y con base al entrenamiento creamos el modelo de clasficación
        entrenamiento = Entrenamiento(self.mat_entrenamiento, indice_valores)
        clasificacion = Clasificacion(entrenamiento, indice_aceptacion)

        tabla_clasificado_vs_real = np.matrix(np.zeros(shape=(self.total_sujs, self.total_sujs)))

        for i in range(0, len(self.indices_imgs_evaluacion)):

            # Obtenemos el sujeto real y el sujeto que corresponde a la clasificacion
            indice_sujeto_real = self.indices_imgs_evaluacion[i]
            indice_sujeto, similitud = clasificacion.ejecutar(self.mat_evaluacion[:, i])

            if indice_sujeto != -1:
                indice_sujeto = self.indices_imgs_entrenamiento[indice_sujeto]
                tabla_clasificado_vs_real[indice_sujeto // 10, indice_sujeto_real // 10] += 1

        return tabla_clasificado_vs_real

    # ------------------------------------------------------------------------------------------------------------------

    def obt_tabla_evaluacion(self, tabla_clasificado_vs_real):

        tabla_evaluacion = np.matrix(np.zeros(shape=(self.total_sujs, 5)))

        for i in range(0, 41):

            vp = tabla_clasificado_vs_real[i, i]
            fp = np.sum(tabla_clasificado_vs_real[i, :]) - vp
            fn = np.sum(tabla_clasificado_vs_real[:, i]) - vp
            tvp = vp / (fn + vp) if (fn + vp) != 0 else 0
            tpp = vp / (vp + fp) if (vp + fp) != 0 else 0

            tabla_evaluacion[i, 0] = vp
            tabla_evaluacion[i, 1] = fp
            tabla_evaluacion[i, 2] = fn
            tabla_evaluacion[i, 3] = tvp
            tabla_evaluacion[i, 4] = tpp

        return tabla_evaluacion

    # ------------------------------------------------------------------------------------------------------------------

    def __str__(self):

        # Colocamos los encabezados de la matriz
        etiquetas_verticales = list(self.coleccion.dic_sujs.values())
        etiquetas_horizontales = ["Sujeto", "VP", "FP", "FN", "TVP", "TPP"]
        tabla_evaluacion = self.tabla_evaluacion.astype(np.str)
        tabla_evaluacion = np.insert(tabla_evaluacion, 0, etiquetas_verticales, axis=1)
        tabla_evaluacion = np.insert(tabla_evaluacion, 0, etiquetas_horizontales, axis=0)

        return str(tabla_evaluacion)

# ----------------------------------------------------------------------------------------------------------------------
