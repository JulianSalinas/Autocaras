# ----------------------------------------------------------------------------------------------------------------------

from coleccion import *

# ----------------------------------------------------------------------------------------------------------------------


class Evaluacion(object):

    def __init__(self, coleccion, entrenamiento, clasificador):

        """
        Clase usada para evaluar la precisión y exhaustividad  del sistema. Se toma un porcentaje de imagenes de la
        colección para entrenar el sistema y otro porcentaje para clasificar (escogidas aleatoriamente respetando
        la cantidad que se deben tomar).
        @param coleccion: Instancia de Coleccion
        @param entrenamiento: Instancia de Entrenamiento
        @param clasificador: Instancia de Clasificador
        """

        # Extraemos la información necesaria de la colección
        self.coleccion = coleccion
        self.total_sujs = coleccion.total_sujs
        self.imgs_x_suj = coleccion.total_imgs//self.total_sujs

        # Obtenemos las claves de las imagenes que son para entrenar y para evaluar
        self.indices_imgs_entrenamiento = entrenamiento.indices_entrenamiento
        self.indices_imgs_evaluacion = \
            np.delete(range(0, coleccion.total_imgs), entrenamiento.indices_entrenamiento)

        # Tabla de sujetos clasificadas vs reales
        self.clasificaciones = self.obt_clasificaciones(clasificador)

        # Tabla donde cada fila corresponde a un sujeto y cada columna
        # contiene los vp, fp, fn, recall, precision
        self.tabla_evaluacion = self.obt_evaluaciones()

        # Fila con los promedios de la tabla de evaluaciones (la anterior)
        self.promedios = np.mean(self.tabla_evaluacion, axis=0)

    # ------------------------------------------------------------------------------------------------------------------

    def obt_clasificaciones(self, clasificador):

        """
        Se obtiene la tabla de sujetos clasificados vs los sujetos reales. Tiene el siguiente formato:

                                suj_real1   suj_real2   suj_realN
            suj_clasificado1        int         int         int
            suj_clasificado2        int         int         int
            suj_clasificadoN        int         int         int

        @param clasificador: Instancia de Clasificador
        @return: npmatrix donde las cada fila corresponde al sujeto clasificado y las columnas a los reales
        """

        mat_imgs = self.coleccion.obt_subconjunto(self.indices_imgs_evaluacion)
        tabla = np.matrix(np.zeros(shape=(self.total_sujs, self.total_sujs)))

        for i in range(0, len(self.indices_imgs_evaluacion)):

            # Obtenemos el sujeto real y el sujeto que corresponde a la clasificador
            indice_suj_real = self.indices_imgs_evaluacion[i]
            indice_suj, sim = clasificador.clasificar(mat_imgs[:, i])

            # Si el sujeto fue clasificado correctamente, lo sumamos a la tabla
            if indice_suj != -1:
                indice_suj = self.indices_imgs_entrenamiento[indice_suj]
                fila = indice_suj // self.imgs_x_suj
                columna = indice_suj_real // self.imgs_x_suj
                tabla[fila, columna] += 1

        return tabla

    # ------------------------------------------------------------------------------------------------------------------

    def obt_evaluaciones(self):

        """
        Obtiene una tabla con las evaluaciones para cada uno de los sujetos (clases) con el siguiente formato:

                        vp,     fp,     fn,     recall,  precision
            sujeto1     float   float   float   float    float
            sujeto2     float   float   float   float    float
            sujetoN     float   float   float   float    float

        @return: npmatriz donde cada fila corresponde a un sujeto (clase) y cada columna a las evaluaciones realizadas
        """

        tabla = np.matrix(np.zeros(shape=(self.total_sujs, 5)))

        for i in range(0, self.total_sujs):

            vp = self.clasificaciones[i, i]
            fp = np.sum(self.clasificaciones[i, :]) - vp
            fn = np.sum(self.clasificaciones[:, i]) - vp
            tvp = vp / (fn + vp) if (fn + vp) != 0 else 0
            tpp = vp / (vp + fp) if (vp + fp) != 0 else 0

            tabla[i, 0] = vp
            tabla[i, 1] = fp
            tabla[i, 2] = fn
            tabla[i, 3] = tvp
            tabla[i, 4] = tpp

        return tabla

    # ------------------------------------------------------------------------------------------------------------------

    def agregar_encabezados(self):

        # Colocamos los encabezados de la matriz
        etiquetas_horizontales = ["VP", "FP", "FN", "Recall", "Precision"]
        etiquetas_verticales = ["Sujeto"] + list(self.coleccion.dic_sujs.values()) + ["Promedio"]
        tabla_evaluacion = self.tabla_evaluacion.astype(np.str)
        tabla_evaluacion = np.insert(tabla_evaluacion, 0, etiquetas_horizontales, axis=0)
        tabla_evaluacion = np.append(tabla_evaluacion, self.promedios.astype(np.str), axis=0)
        tabla_evaluacion = np.insert(tabla_evaluacion, 0, etiquetas_verticales, axis=1)
        return tabla_evaluacion

    # ------------------------------------------------------------------------------------------------------------------

    def __str__(self):
        tabla_evaluacion = self.agregar_encabezados()
        return str(tabla_evaluacion)

# ----------------------------------------------------------------------------------------------------------------------


