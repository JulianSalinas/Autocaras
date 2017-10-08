# ----------------------------------------------------------------------------------------------------------------------

import re

from entrenamient import *
from coleccion import *


# ----------------------------------------------------------------------------------------------------------------------


class DaoIndice:

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def guardar_coleccion(sufijo, coleccion):

        """
        Guarda en un archivo la informacion de una coleccion con el objetivo de ser utilizada a futuro.
        @param sufijo: sufijo a concantenar a cada archivo generado para poder identificarlos.
        @param coleccion: objeto Coleccion del cual se va a extraer la informacion a guardar.
        @return: no retorna algun valor.
        """

        # Guardar informacion sobre el objeto coleccion
        f_coleccion = open('..\\..\\Index\\coleccion_' + sufijo + '.txt', 'w')
        coleccion = {'ruta_datos': coleccion.ruta_datos,
                     'regex_sujs': coleccion.regex_sujs,
                     'regex_imgs': coleccion.regex_imgs,
                     'dic_sujs': coleccion.dic_sujs,
                     'dic_imgs': coleccion.dic_imgs,
                     'alto_imgs': coleccion.alto_img,
                     'ancho_imgs': coleccion.ancho_img,
                     'total_imgs': coleccion.total_imgs,
                     'pixeles_img': coleccion.pixeles_img}
        f_coleccion.write(str(coleccion))
        f_coleccion.close()

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def guardar_entrenamiento(sufijo, entrenamiento):

        """
        Guarda la información del entrenamiento realizado con el objetivo de realizar busquedas sobre esta informacion
        sin necesidad de volver a ser calculada.
        @param sufijo: sufijo a concatenar a cada uno de los archivos generados para poder identificarlos.
        @param entrenamiento: objeto Entrenamiento del cual se extraera la informacion.
        @return: no retorna algun valor.
        """

        sufijo += '.npy'
        prefijo = '..\\..\\Index\\'

        np.save(prefijo + 'indices_entrenamiento_' + sufijo, entrenamiento.indices_entrenamiento)
        np.save(prefijo + 'muestra_promedio_' + sufijo, entrenamiento.muestra_promedio)
        np.save(prefijo + 'autoespacio_' + sufijo, entrenamiento.autoespacio)
        np.save(prefijo + 'proyecciones_' + sufijo, entrenamiento.proyecciones)

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def leer_indexado(sufijo):

        """
        Lee los archivos indexados y los carga en memoria mediante objetos.
        @param sufijo: sufijo con el que se guardaron los archivos indexados
        @return: tupla (objeto_coleccion, objeto_entrenamiento) con los valores asignados y listos para hacer una
        clasificador
        """

        prefijo = '..\\..\\Index\\'

        # Lectura del archivo que contiene la informacion de la coleccion
        f_coleccion = open(prefijo + 'coleccion_' + sufijo + '.txt', 'r')
        dicc_coleccion = eval(f_coleccion.read())
        f_coleccion.close()

        # Construir objeto de coleccion
        coleccion = Coleccion(dicc_coleccion['ruta_datos'], dicc_coleccion['regex_sujs'], dicc_coleccion['regex_imgs'])
        coleccion.dic_imgs = dicc_coleccion['dic_imgs']
        coleccion.alto_img = dicc_coleccion['alto_imgs']
        coleccion.ancho_img = dicc_coleccion['ancho_imgs']
        coleccion.total_imgs = dicc_coleccion['total_imgs']
        coleccion.pixeles_img = dicc_coleccion['pixeles_img']

        # Construir objeto de entrenamiento
        sufijo += '.npy'
        entrenamiento = Entrenamiento
        entrenamiento.indices_entrenamiento = np.load(prefijo + 'indices_entrenamiento_' + sufijo)
        entrenamiento.muestra_promedio = np.load(prefijo + 'muestra_promedio_' + sufijo)
        entrenamiento.autoespacio = np.load(prefijo + 'autoespacio_' + sufijo)
        entrenamiento.proyecciones = np.load(prefijo + 'proyecciones_' + sufijo)

        return coleccion, entrenamiento

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def guardar_presicion(nombre_archivo, evaluacion):

        """
        Guarda los resultados de la evaluacion del sistema en un archivo en formato csv.
        @param nombre_archivo: nombre con el cual se va a guardar la evaluacion actual.
        @param evaluacion: objeto evaluacion con los valores calculados
        @return: no retorna algun valor.
        """

        tabla_evaluacion = evaluacion.agregar_encabezados()
        f_evaluacion = open('..\\..\\Evaluaciones\\' + nombre_archivo + '.csv', 'w')

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
