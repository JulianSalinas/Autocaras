# ----------------------------------------------------------------------------------------------------------------------

from os.path import *

# ----------------------------------------------------------------------------------------------------------------------


class Configuracion(object):

    """ Sirve para proveer las rutas que necesitan cada uno de los modulos del sistema """

    RUTA_RAIZ = split(dirname(abspath(__file__)))[0]
    RUTA_INDICE = join(RUTA_RAIZ, "controlador", "pickle")
    RUTA_CONFIG = join(RUTA_INDICE, "config.pkl")
    RUTA_DATOS = join(RUTA_RAIZ, "datos")
    RUTA_MEDIA = join(RUTA_RAIZ, "vista", "media")
    RUTA_COLECCION = join(RUTA_INDICE, "coleccion.pkl")
    RUTA_ENTRENAMIENTO = join(RUTA_INDICE, "entrenamiento.pkl")

    REGEX_SUJS = "s[0-9]*"
    REGEX_IMGS = "\\[0-9]*.pgm"
    SUJ_DESCONOCIDO = join(RUTA_DATOS, "otros")
    IMG_DESCONOCIDA = join(SUJ_DESCONOCIDO, "desconocido.pgm")

# ----------------------------------------------------------------------------------------------------------------------
