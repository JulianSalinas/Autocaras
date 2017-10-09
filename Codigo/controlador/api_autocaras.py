# ----------------------------------------------------------------------------------------------------------------------

from controlador.controlador import *

# ----------------------------------------------------------------------------------------------------------------------


class APIAutocaras(object):

    def __init__(self):

        self.ctrl = Controlador()

    # ------------------------------------------------------------------------------------------------------------------

    def indexar_coleccion(self):

        """ Indexa la colección de imagenes con base al archivo configuracion.py"""

        self.ctrl.indexar_coleccion()

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_entrenamiento(self, porcentaje_coleccion=80, porcentaje_valores=85, porcentaje_aceptacion=75):

        """
        Ejecuta el entrenamiento del sistema
        @param porcentaje_coleccion: Porcentaje de la colección que se usará para realizar el entrenamiento
        @param porcentaje_valores: Porcentaje de valores (autocaras o componentes) que se desean conservar
        @param porcentaje_aceptacion: Procentaje de aceptación mínimo para que el clasificador reconozca un sujeto
        @return no retorna algun valor
        """

        self.ctrl.ejecutar_entrenamiento(porcentaje_coleccion, porcentaje_valores, porcentaje_aceptacion)

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_clasificacion(self, ruta_img_buscada):

        """
        Ejecuta la clasificación para una imagen
        @param ruta_img_buscada: ruta de la imagen desconocida que se desea clasificar
        @return: sujeto, ruta_img_mas_similar, grado_similitud
        """

        return self.ctrl.ejecutar_clasificacion(ruta_img_buscada)

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_evaluacion(self, ruta_archivo='AT&T'):

        """
        Crea un informe con la evaluación del sistema
        @param ruta_archivo: Ruta absoluta del archivo a crear para guardar el informe de la evaluación
        @return no retorna algun valor.
        """

        self.ctrl.ejecutar_evaluacion(ruta_archivo)

# ----------------------------------------------------------------------------------------------------------------------
