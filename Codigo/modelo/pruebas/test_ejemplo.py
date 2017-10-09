import os
from modelo.utilitarios.fuentes import *
from controlador.api_autocaras import *

# TODO: Encontrar los valores óptimos para el porcentaje de valores a conservar y el mínimo de aceptación

api = APIAutocaras()


def ejemplo(ruta_img_desconocida):

    print(Fuente.VERDE + "\nSujeto buscado: " + ruta_img_desconocida + Fuente.FIN)

    try:

        sujeto, img_encontrada, similitud = api.ejecutar_clasificacion(ruta_img_desconocida)

        if sujeto is None:
            sujeto = "Desconocido"
            img_encontrada = "Indefinida"

        print("----------------------------------------------------------")
        print("Similitud: " + str(round(similitud*100, 2)) + "%")
        print("Sujeto encontrado: " + sujeto)
        print("Imagen más cercana: " + img_encontrada)
        print("----------------------------------------------------------\n")

    except IOError as error:

        print("----------------------------------------------------------")
        print("Error al leer la imagen: \n", error.strerror)
        print("----------------------------------------------------------\n")

suj = os.path.join(Config.RUTA_DATOS, "otros", "1_1.pgm")

ejemplo(suj)
# ejemplo("../../datos/otros/13_4.pgm")
# ejemplo("../../datos/otros/26_7.pgm")
# ejemplo("../../datos/otros/41_8.pgm")
# ejemplo("../../datos/otros/cara1.png")
# ejemplo("../../datos/otros/cara2.png")
# ejemplo("../../datos/otros/cara3.png")
# ejemplo("../../datos/otros/cara4.png")
# ejemplo("../../datos/otros/cara5.png")
# ejemplo("../../datos/otros/nocara1.png")
# ejemplo("../../datos/otros/nocara2.png")
# ejemplo("../../datos/otros/nocara3.png")
# ejemplo("../../datos/otros/nocara4.png")
# ejemplo("../../datos/otros/nocara5.png")