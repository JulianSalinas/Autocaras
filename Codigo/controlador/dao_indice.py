# ----------------------------------------------------------------------------------------------------------------------

import re

from modelo.entrenamiento import *
from modelo.coleccion import *


# ----------------------------------------------------------------------------------------------------------------------


class DaoIndice:

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def guardar_coleccion(coleccion):

        """
        Guarda en un archivo la informacion de una coleccion con el objetivo de ser utilizada a futuro.
        @return: no retorna algun valor.
        """

        f_coleccion = open(Config.RUTA_COLECCION, 'w')
        coleccion = {'dic_sujs': coleccion.dic_sujs,
                     'dic_imgs': coleccion.dic_imgs,
                     'alto_imgs': coleccion.alto_img,
                     'ancho_imgs': coleccion.ancho_img,
                     'total_imgs': coleccion.total_imgs,
                     'pixeles_img': coleccion.pixeles_img}
        f_coleccion.write(str(coleccion))
        f_coleccion.close()

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def guardar_entrenamiento(entrenamiento):

        """
        Guarda la información del entrenamiento realizado con el objetivo de realizar busquedas sobre esta informacion
        sin necesidad de volver a ser calculada.
        @param entrenamiento: objeto Entrenamiento del cual se extraera la informacion.
        @return: no retorna algun valor.
        """

        np.save(Config.RUTA_INDICES_ENTRENAMIENTO, entrenamiento.indices_entrenamiento)
        np.save(Config.RUTA_PROMEDIO_ENTRENAMIENTO, entrenamiento.muestra_promedio)
        np.save(Config.RUTA_AUTOESPACIO_ENTRENAMIENTO, entrenamiento.autoespacio)
        np.save(Config.RUTA_PROYECCIONES_ENTRENAMIENTO, entrenamiento.proyecciones)

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def guardar_configuracion(ruta_configuracion):

        # np.save(Config.RUTA_INDICES_ENTRENAMIENTO, entrenamiento.indices_entrenamiento)
        # np.save(Config.RUTA_PROMEDIO_ENTRENAMIENTO, entrenamiento.muestra_promedio)
        # np.save(Config.RUTA_AUTOESPACIO_ENTRENAMIENTO, entrenamiento.autoespacio)
        # np.save(Config.RUTA_PROYECCIONES_ENTRENAMIENTO, entrenamiento.proyecciones)
        return None

    @staticmethod
    def cargar_ultima_configuracion(ruta_configuracion):

        return None

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def cargar_ultima_coleccion():

        """
        Lee los elementos indexados (diccionarios) y los carga en memoria mediante un objeto Coleccion
        :return: Instancia de la clase Coleccion
        """

        # Lectura del archivo que contiene la informacion de la coleccion
        f_coleccion = open(Config.RUTA_COLECCION, 'r')
        dicc_coleccion = eval(f_coleccion.read())
        f_coleccion.close()

        # Construir objeto de coleccion
        coleccion = Coleccion()
        coleccion.dic_sujs = dicc_coleccion['dic_sujs']
        coleccion.dic_imgs = dicc_coleccion['dic_imgs']
        coleccion.alto_img = dicc_coleccion['alto_imgs']
        coleccion.ancho_img = dicc_coleccion['ancho_imgs']
        coleccion.total_imgs = dicc_coleccion['total_imgs']
        coleccion.pixeles_img = dicc_coleccion['pixeles_img']

        return coleccion

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def cargar_ultimo_entrenamiento():

        """
        Lee los elementos indexados como los indices de la coleccion utilizados, muestra promedio, autoespacio y
        proyecciones y los carga en memoria mediante un objeto Entrenamiento
        :return: Instancia de la clase Entrenamiento
        """

        # Construir objeto de entrenamiento
        entrenamiento = Entrenamiento
        entrenamiento.indices_entrenamiento = np.load(Config.RUTA_INDICES_ENTRENAMIENTO)
        entrenamiento.muestra_promedio = np.load(Config.RUTA_PROMEDIO_ENTRENAMIENTO)
        entrenamiento.autoespacio = np.load(Config.RUTA_AUTOESPACIO_ENTRENAMIENTO)
        entrenamiento.proyecciones = np.load(Config.RUTA_PROYECCIONES_ENTRENAMIENTO)

        return entrenamiento

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def guardar_evaluacion(nombre_archivo, evaluacion):

        """
        Guarda los resultados de la evaluacion del sistema en un archivo en formato csv.
        @param nombre_archivo: nombre con el cual se va a guardar la evaluacion actual.
        @param evaluacion: objeto evaluacion con los valores calculados
        @return: no retorna algun valor.
        """

        tabla_evaluacion = evaluacion.agregar_encabezados()
        f_evaluacion = open(nombre_archivo + '.csv', 'w')

        fin_fila = 0
        for x in np.nditer(tabla_evaluacion):
            linea = str(x)

            # Extraer solamente el nombre de sujeto
            if fin_fila == 0:
                sujeto = re.findall(r's\d+', str(x))
                if len(sujeto) > 0:
                    linea = sujeto[0]

            # Verificar si es necesario el cambio de fila
            if fin_fila == 5:
                linea += '\n'
                fin_fila = 0
            else:
                linea += ','
                fin_fila += 1

            f_evaluacion.write(linea)
        f_evaluacion.close()

# ----------------------------------------------------------------------------------------------------------------------
