import subprocess
from modelo.utilitarios.fuentes import *
from controlador.controlador import *
from controlador.api_autocaras import *

# TODO: Encontrar los valores óptimos para el porcentaje de valores a conservar y el mínimo de aceptación

api = APIAutocaras()
api.ejecutar_entrenamiento(porcentaje_coleccion=50)


def ejemplo(ruta_img_desconocida):

    print(Fuente.VERDE + "\nSujeto buscado: " + ruta_img_desconocida + Fuente.FIN)

    try:
        resultado = api.ejecutar_clasificacion(ruta_img_desconocida)

        print("----------------------------------------------------------")
        print("Similitud: " + resultado["grado_similitud"])
        print("Sujeto encontrado: " + resultado["sujeto_identificado"])
        print("Imagen más cercana: " + resultado["img_similar"])
        print("----------------------------------------------------------\n")

    except IOError as error:

        print("----------------------------------------------------------")
        print("Error al leer la imagen: \n", error.strerror)
        print("----------------------------------------------------------\n")


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

api.ejecutar_evaluacion("eval")


print(os.path.join(Configuracion.RUTA_MEDIA, "eval.cvs"))
subprocess.call("explorer " + os.path.join(Configuracion.RUTA_MEDIA, "eval.cvs"), shell=True)
