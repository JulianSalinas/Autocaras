# ----------------------------------------------------------------------------------------------------------------------

import pip
from os.path import *

# ----------------------------------------------------------------------------------------------------------------------

class Config:

    RUTA_RAIZ = split(dirname(abspath(__file__)))[0]
    RUTA_DATOS = join(RUTA_RAIZ, "datos")
    RUTA_MEDIA = join(RUTA_RAIZ, "vista", "media")
    RUTA_INDICE = join(RUTA_DATOS, "indice")
    RUTA_COLECCION = join(RUTA_DATOS, "indice", "coleccion.txt")

    RUTA_ENTRENAMIENTO = join(RUTA_INDICE, "entrenamiento")
    RUTA_INDICES_ENTRENAMIENTO = join(RUTA_ENTRENAMIENTO, 'indices.npy')
    RUTA_PROMEDIO_ENTRENAMIENTO = join(RUTA_ENTRENAMIENTO, 'promedio.npy')
    RUTA_AUTOESPACIO_ENTRENAMIENTO = join(RUTA_ENTRENAMIENTO, 'autoespacio.npy')
    RUTA_PROYECCIONES_ENTRENAMIENTO = join(RUTA_ENTRENAMIENTO, 'proyecciones.npy')

    REGEX_SUJS = "s[0-9]*"
    REGEX_IMGS = "\\[0-9]*.pgm"
    SUJ_DESCONOCIDO = join(RUTA_DATOS, "otros")
    IMG_DESCONOCIDA = join(SUJ_DESCONOCIDO, "desconocido.pgm")

config = {
    "RUTA_RAIZ":  Config.RUTA_RAIZ,
    "RUTA_DATOS": join(Config.RUTA_RAIZ, "datos"),
    "RUTA_MEDIA": join(Config.RUTA_RAIZ, "vista", "media"),
    "REGEX_SUJS": Config.REGEX_SUJS,
    "REGEX_IMGS": Config.REGEX_IMGS,
    "SUJ_DESCONOCIDO": join(Config.RUTA_DATOS, "otros"),
    "IMG_DESCONOCIDA": join(Config.SUJ_DESCONOCIDO, "desconocido.pgm")
}


# ----------------------------------------------------------------------------------------------------------------------


def instalar_dependencias():
    try:
        pip.main(["install", "numpy", "django", "opencv-python"])
    except OSError:
        print("Intente instalar manualmente con permisos de administrador: ")
        print("\n > pip install numpy django opencv-python")

# ----------------------------------------------------------------------------------------------------------------------
