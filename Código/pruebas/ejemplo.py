from controlador import *
from imprimir import *

# TODO: Encontrar los valores óptimos para el porcentaje de valores a conservar y el mínimo de aceptación

ctrl = Controlador()
ctrl.indexar_coleccion(ruta_datos="..\\..\\Datos", regex_sujs="s[0-9]*", regex_imgs="\\[1-4].pgm")
ctrl.ejecutar_entrenamiento(indice_valores=0.85, indice_aceptacion=0.75)


def ejemplo(ruta_img_desconocida):

    imprimir_verde("\nSujeto buscado: " + ruta_img_desconocida)

    try:

        sujeto, img, similitud = ctrl.ejecutar_clasificacion(ruta_img_desconocida)
        imprimir_verde("----------------------------------------------------------")
        print("Similitud: " + str(similitud))
        print("Sujeto encontrado: " + sujeto)
        print("Imagen más cercana: " + img)
        imprimir_verde("----------------------------------------------------------")

    except IOError:

        imprimir_verde("----------------------------------------------------------")
        print("Error al leer la imagen")
        imprimir_verde("----------------------------------------------------------")

    except Exception as e:

        imprimir_verde("----------------------------------------------------------")
        print(e)
        imprimir_verde("----------------------------------------------------------")

ejemplo("..\\..\\Datos\\otros\\1_1.pgm")
ejemplo("..\\..\\Datos\\otros\\13_4.pgm")
ejemplo("..\\..\\Datos\\otros\\26_7.pgm")
ejemplo("..\\..\\Datos\\otros\\41_8.pgm")
ejemplo("..\\..\\Datos\\otros\\cara1.png")
ejemplo("..\\..\\Datos\\otros\\cara2.png")
ejemplo("..\\..\\Datos\\otros\\cara3.png")
ejemplo("..\\..\\Datos\\otros\\cara4.png")
ejemplo("..\\..\\Datos\\otros\\cara5.png")
ejemplo("..\\..\\Datos\\otros\\nocara1.png")
ejemplo("..\\..\\Datos\\otros\\nocara2.png")
ejemplo("..\\..\\Datos\\otros\\nocara3.png")
ejemplo("..\\..\\Datos\\otros\\nocara4.png")
ejemplo("..\\..\\Datos\\otros\\nocara5.png")

