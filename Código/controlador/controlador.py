# ----------------------------------------------------------------------------------------------------------------------

from clasificacion import *
from entrenamiento import *
from evaluacion import *
from coleccion import *

# ----------------------------------------------------------------------------------------------------------------------


class Controlador(object):

    def __init__(self):

        """
        Clase principal del sistema, aquí se reunen los casos de uso, como por ejemplo, entrenar el sistema, realizar
        la clasificación de imagenes desconocidas. Se debe tomar en cuenta las siguientes consideraciones:
            1. Indexar la colección de imágenes implica tener que re-entrenar el sistema.
            2. Entrenar el sistema requiere refrescar el modelo para clasificación.
            3. Antes de usar el modelo de clasificación el sistema debe de haber sido entrenado previamente.
            4. Antes de evaluar al sistema se tiene que haber indexado la colección de imagenes
        """

        self.coleccion = None
        self.entrenamiento = None
        self.clasificacion = None
        self.evaluacion = None

    # ------------------------------------------------------------------------------------------------------------------

    def indexar_coleccion(self, ruta_datos, regex_sujs, regex_imgs):

        """
        Indexa la colección de imagenes que se encuentre en una ruta dada. Se usa una expresión regular para seleccionar
        las carpetas que pertencen a sujetos dentro de la colección, de igual forma para determinar que archivos se
        deben tomar en cuenta para cada uno de estos sujetos.
        @param ruta_datos: Ruta donde estan las imagenes.
        @param regex_sujs: Expresión regula que indique que carpetas corresponden a sujetos.
        @param regex_imgs: Expresión regula que indique archivos corresponden a la imagen de un sujeto.
        """

        self.coleccion = Coleccion(ruta_datos, regex_sujs, regex_imgs)

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_entrenamiento(self, indice_valores, indice_aceptacion):

        """
        Ejecuta el entrenamiento del sistema. Se debe indicar la cantidad de valores (autocaras) que se desean conservar
        por medio de un índice, por ejemplo si la cantidad de muestras es 100 y se especifica 0.7 la cantidad de
        autocaras a conservar serán 70. Además, se debe indicar el índice de aceptación para el clasificador, si la
        similitud de obtenida es menor que dicho índice significa que la imagen no se encuentra en el espacio creado.
        @param indice_valores: Índice que indica la cantidad de valores (autocaras) a conservar.
        @param indice_aceptacion:Índice mínimo para considerar que un sujeto desconocido se encuentra dentro del espacio
        """

        muestras = self.coleccion.obt_matriz_muestras()
        self.entrenamiento = Entrenamiento(muestras, indice_valores)

        # Indexa los archivos para clasificaciones futuras
        self.coleccion.indexar('AT&T')
        self.entrenamiento.indexar('AT&T')

        self.clasificacion = Clasificacion(self.entrenamiento, indice_aceptacion)


    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_clasificacion(self, ruta_img_desconocida):

        """
        Realizar la clasificación para una imagen mediante el método del centroide más cercano.
        @param ruta_img_desconocida: ruta de la imagen a clasificar.
        @return: Tupla(Su, Im, Si) donde Su es la ruta del sujeto, Im la ruta de la imagen con la que se encontró
        mayor parecido y Si el grado de similitud encontrado.
        """

        img = cv.imread(ruta_img_desconocida, 0)
        if img is not None:
            indice, similitud = self.clasificacion.ejecutar(img)
            sujeto, img = self.coleccion.consultar_img(indice)
            return sujeto, img, similitud
        raise IOError

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_evaluacion(self, indice_evaluacion):

        """
        Ejecuta la evaluación del sistema.
        @param indice_evaluacion: Índice que representa la cantidad de elementos de la colección que se usarán para
        realizar la evaluación del sistema. 1 - indice_evaluacion será la cantidad de imagenes de la colección
        @return:
        """

        self.evaluacion = Evaluacion(self.coleccion, indice_evaluacion, 0.85, 0.70)
        return self.evaluacion

# ----------------------------------------------------------------------------------------------------------------------
