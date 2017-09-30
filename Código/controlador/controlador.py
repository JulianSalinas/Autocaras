# ----------------------------------------------------------------------------------------------------------------------

from clasificacion import *
from entrenamiento import *
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
        """

        self.coleccion = None
        self.entrenamiento = None
        self.clasificacion = None

    # ------------------------------------------------------------------------------------------------------------------

    def indexar_coleccion(self, ruta_datos, regex_sujs, regex_imgs):
        self.coleccion = Coleccion(ruta_datos, regex_sujs, regex_imgs)

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_entrenamiento(self, porcentaje_valores, min_aceptacion):
        muestras = self.coleccion.obt_matriz_muestras()
        cant_valores = int(self.coleccion.total_imgs * (porcentaje_valores/100))
        self.entrenamiento = Entrenamiento(muestras, cant_valores)
        self.clasificacion = Clasificacion(self.entrenamiento, min_aceptacion)

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_clasificacion(self, ruta_img_desconocida):
        img = cv.imread(ruta_img_desconocida, 0)
        if img is not None:
            indice, distancia = self.clasificacion.ejecutar(img)
            sujeto, img = self.coleccion.consultar(indice)
            return sujeto, img, distancia
        raise IOError

# ----------------------------------------------------------------------------------------------------------------------
