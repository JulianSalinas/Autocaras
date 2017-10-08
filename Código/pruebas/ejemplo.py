from fachada_autocaras import *
from imprimir import *

# TODO: Encontrar los valores óptimos para el porcentaje de valores a conservar y el mínimo de aceptación

api = FachadaAutocaras()


def ejemplo(ruta_img_desconocida):

    imprimir_verde("\nSujeto buscado: " + ruta_img_desconocida)

    try:

        sujeto, img_encontrada, similitud, img_buscada = api.ejecutar_clasificacion(ruta_img_desconocida)

        if sujeto is None:
            sujeto = "Desconocido"
            img_encontrada = "Indefinida"

        imprimir_verde("----------------------------------------------------------")
        print("Similitud: " + str(round(similitud*100, 2)) + "%")
        print("Sujeto encontrado: " + sujeto)
        print("Imagen más cercana: " + img_encontrada)
        print("Imagen buscada: " + img_buscada)
        imprimir_verde("----------------------------------------------------------\n")

    except IOError:

        imprimir_verde("----------------------------------------------------------")
        print("Error al leer la imagen")
        imprimir_verde("----------------------------------------------------------\n")


ejemplo("../../Datos/otros/1_1.pgm")
# ejemplo("../../Datos/otros/13_4.pgm")
# ejemplo("../../Datos/otros/26_7.pgm")
# ejemplo("../../Datos/otros/41_8.pgm")
# ejemplo("../../Datos/otros/cara1.png")
# ejemplo("../../Datos/otros/cara2.png")
# ejemplo("../../Datos/otros/cara3.png")
# ejemplo("../../Datos/otros/cara4.png")
# ejemplo("../../Datos/otros/cara5.png")
# ejemplo("../../Datos/otros/nocara1.png")
# ejemplo("../../Datos/otros/nocara2.png")
# ejemplo("../../Datos/otros/nocara3.png")
# ejemplo("../../Datos/otros/nocara4.png")
# ejemplo("../../Datos/otros/nocara5.png")