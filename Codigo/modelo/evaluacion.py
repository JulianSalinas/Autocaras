# ----------------------------------------------------------------------------------------------------------------------

from modelo.coleccion import *

# ----------------------------------------------------------------------------------------------------------------------

"""
@author Julian Salinas, Armando Lopez, Andrey Mendoza, Brandon Dinarte
@version 1.6.49
"""

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

        self.clasificador = clasificador

        # Obtenemos las claves de las imagenes que son para entrenar y para evaluar
        self.indices_imgs_entrenamiento = entrenamiento.indices_entrenamiento
        self.indices_imgs_evaluacion = \
            np.delete(range(0, coleccion.total_imgs), entrenamiento.indices_entrenamiento)

        # Extraemos la información necesaria de la colección
        self.coleccion = coleccion
        self.total_sujs = coleccion.total_sujs
        self.imgs_x_suj = self.coleccion.total_imgs // self.total_sujs

        # Tabla de sujetos clasificadas vs reales
        self.tabla_clasificaciones = self.obt_clasificaciones()

        # Tabla donde cada fila corresponde a un sujeto y cada columna
        # contiene los vp, fp, fn, recall, precision
        self.tabla_evaluacion = self.obt_evaluaciones()

        # Fila con los promedios de la tabla de evaluaciones (la anterior)
        self.promedios = np.mean(self.tabla_evaluacion, axis=0)

    # ------------------------------------------------------------------------------------------------------------------

    def obt_clasificaciones(self):

        """
        Se obtiene la tabla de sujetos clasificados vs los sujetos reales. Tiene el siguiente formato:

                                suj_real1   suj_real2   suj_realN
            suj_clasificado1        int         int         int
            suj_clasificado2        int         int         int
            suj_clasificadoN        int         int         int

        @return: npmatrix donde las cada fila corresponde al sujeto clasificado y las columnas a los reales
        """

        mat_imgs = self.coleccion.obt_subconjunto(self.indices_imgs_evaluacion)
        tabla = np.matrix(np.zeros(shape=(self.total_sujs, self.total_sujs)))

        for i in range(0, len(self.indices_imgs_evaluacion)):

            indice_img_real = self.indices_imgs_evaluacion[i]

            # Clasificamos la imagen real esperando que nos devuelva el mismo
            # indice donde se encuentra en la coleccion para obtener un VP
            indice_img_similar = self.clasificador.clasificar(mat_imgs[:, i])[0]

            # Si el sujeto fue clasificado correctamente, lo podemos sumar a la tabla
            if indice_img_similar != -1:
                indice_img_similar = self.indices_imgs_entrenamiento[indice_img_similar]

                # Con eseto obtenemos la posicion del sujeto
                fila = indice_img_similar // self.imgs_x_suj
                columna = indice_img_real // self.imgs_x_suj

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

            vp = self.tabla_clasificaciones[i, i]
            fp = np.sum(self.tabla_clasificaciones[i, :]) - vp
            fn = np.sum(self.tabla_clasificaciones[:, i]) - vp
            tvp = vp / (fn + vp) if (fn + vp) != 0 else 0
            tpp = vp / (vp + fp) if (vp + fp) != 0 else 0

            tabla[i, 0] = vp
            tabla[i, 1] = fp
            tabla[i, 2] = fn
            tabla[i, 3] = tvp
            tabla[i, 4] = tpp

        return tabla

    # ------------------------------------------------------------------------------------------------------------------

    def agregar_encabezados_tabla_clasificaciones(self):

        sujetos = list(self.coleccion.dic_sujs.values())
        for i in range(len(sujetos)):
            sujetos[i] = os.path.split(sujetos[i])[1]

        tabla_clasificaciones = self.tabla_clasificaciones.astype(np.str)
        tabla_clasificaciones = np.insert(tabla_clasificaciones, 0, sujetos, axis=0)
        tabla_clasificaciones = np.insert(tabla_clasificaciones, 0, [""] + sujetos, axis=1)
        return tabla_clasificaciones

    # ------------------------------------------------------------------------------------------------------------------

    def agregar_encabezados_tabla_evaluaciones(self):

        # Colocamos los encabezados de la matriz
        etiquetas_horizontales = ["VP", "FP", "FN", "Recall", "Precision"]

        sujetos = list(self.coleccion.dic_sujs.values())
        for i in range(len(sujetos)):
            sujetos[i] = os.path.split(sujetos[i])[1]

        etiquetas_verticales = np.array(["Sujeto"] + sujetos + ["Promedio"])
        tabla_evaluacion = self.tabla_evaluacion.astype(np.str)
        tabla_evaluacion = np.insert(tabla_evaluacion, 0, etiquetas_horizontales, axis=0)
        tabla_evaluacion = np.append(tabla_evaluacion, self.promedios.astype(np.str), axis=0)
        tabla_evaluacion = np.insert(tabla_evaluacion, 0, etiquetas_verticales, axis=1)
        return tabla_evaluacion

# ----------------------------------------------------------------------------------------------------------------------


