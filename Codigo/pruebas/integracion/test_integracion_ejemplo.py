# ----------------------------------------------------------------------------------------------------------------------

import subprocess

from controlador.api_autocaras import *
from modelo.utilitarios.fuentes import *

# ----------------------------------------------------------------------------------------------------------------------

# TODO: Encontrar los valores óptimos para el porcentaje de valores a conservar y el mínimo de aceptación

api = APIAutocaras()
api.indexar_coleccion(Configuracion.RUTA_DATOS)
resultado = api.ejecutar_entrenamiento(porcentaje_coleccion=50, porcentaje_aceptacion=0)

print(Fuente.VERDE + "\nImagenes usadas para el entrenamiento" + Fuente.FIN)
print(resultado["imgs_usadas"])

print(Fuente.VERDE + "Imagenes ignoradas para el entrenamiento (que se usarán para evaluar el sistema)" + Fuente.FIN)
print(resultado["imgs_sin_usar"])

# ----------------------------------------------------------------------------------------------------------------------

def ejemplo(ruta_img_desconocida):

    print(Fuente.VERDE + "\nSujeto buscado: " + ruta_img_desconocida + Fuente.FIN)

    try:
        resultado = api.ejecutar_clasificacion(ruta_img_desconocida)

        if resultado["estado"] != "ERROR":
            print("----------------------------------------------------------")
            print("Similitud: " + resultado["grado_similitud"])
            print("Sujeto encontrado: " + resultado["sujeto_identificado"])
            print("Imagen más cercana: " + resultado["img_similar"])
            print("----------------------------------------------------------\n")
        else:
            print("----------------------------------------------------------")
            print("Mensaje: " + resultado["mensaje"])
            print("Detalles del error: " + resultado["detalles"])
            print("----------------------------------------------------------\n")

    except IOError as error:

        print("----------------------------------------------------------")
        print("Error al leer la imagen: \n", error.strerror)
        print("----------------------------------------------------------\n")

# ----------------------------------------------------------------------------------------------------------------------


ejemplo("../../datos/otros/1_1.pgm")
ejemplo("../../datos/otros/13_4.pgm")
ejemplo("../../datos/otros/26_7.pgm")
ejemplo("../../datos/otros/41_8.pgm")
ejemplo("../../datos/otros/cara1.png")
ejemplo("../../datos/otros/cara2.png")
ejemplo("../../datos/otros/cara3.png")
ejemplo("../../datos/otros/cara4.png")
ejemplo("../../datos/otros/cara5.png")
ejemplo("../../datos/otros/nocara1.png")
ejemplo("../../datos/otros/nocara2.png")
ejemplo("../../datos/otros/nocara3.png")
ejemplo("../../datos/otros/nocara4.png")
ejemplo("../../datos/otros/nocara5.png")

# ----------------------------------------------------------------------------------------------------------------------

api.ejecutar_evaluacion(Configuracion.RUTA_EVALUACION)
subprocess.call("explorer " + Configuracion.RUTA_EVALUACION, shell=True)

# ----------------------------------------------------------------------------------------------------------------------
