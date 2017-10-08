# ----------------------------------------------------------------------------------------------------------------------

from controlador import *

# ----------------------------------------------------------------------------------------------------------------------


class FachadaAutocaras(object):

    def __init__(self):

        self.ctrl = Controlador()

    # ------------------------------------------------------------------------------------------------------------------

    def indexar_coleccion(self, ruta_datos="..\\..\\Datos", regex_sujs="s[0-9]*", regex_imgs="\\[0-9]*.pgm"):

        """
        Indexa la colección de imagenes que se encuentre en una ruta dada
        NOTA: No es necesario que se utilice esta función a menos que la
        ruta de los datos sea diferente a la que se tiene por defecto
        @param ruta_datos: Ruta donde estan las imagenes
        @param regex_sujs: Expresión regula que indique que carpetas corresponden a sujetos
        @param regex_imgs: Expresión regula que indique archivos corresponden a la imagen de un sujeto
        @return no retorna algun valor.
        """

        self.ctrl.indexar_coleccion(ruta_datos, regex_sujs, regex_imgs)

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_entrenamiento(self, porcentaje_coleccion=80, porcentaje_valores=85, porcentaje_aceptacion=75):

        """
        Ejecuta el entrenamiento del sistema
        NOTA: No es necesario ejecutar esta función si los valores son iguales a los que se tiene por defecto
        @param porcentaje_coleccion: Porcentaje de la colección que se usará para realizar el entrenamiento
        @param porcentaje_valores: Porcentaje de valores (autocaras o componentes) que se desean conservar
        @param porcentaje_aceptacion: Procentaje de aceptación mínimo para que el clasificador reconozca que una imagen
        desconocida se encuentra dentro del autoespacio
        @return no retorna algun valor.
        """

        self.ctrl.ejecutar_entrenamiento(porcentaje_coleccion, porcentaje_valores, porcentaje_aceptacion)

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_clasificacion(self, ruta_img_buscada):

        """
        Ejecuta la clasificación para una imagen
        NOTA: Se enviar la imagen "en bruto", abierta con opencv o simplemente la ruta de dicha imagen
        @param ruta_img_buscada: ruta de la imagen desconocida que se desea clasificar
        @return: sujeto, ruta_img_mas_similar, grado_similitud, ruta_img_buscada
        """

        return self.ctrl.ejecutar_clasificacion(ruta_img_buscada)

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_evaluacion(self, nombre_archivo='AT&T'):

        """
        Crea un informe con la evaluación del sistema
        NOTA: Solamente crea un archivo dentro de la carpeta Index del proyecto
        @param nombre_archivo: Ruta absoluta del archivo a crear para guardar el informe de la evaluación
        @return no retorna algun valor.
        """

        self.ctrl.ejecutar_evaluacion(nombre_archivo)

# ----------------------------------------------------------------------------------------------------------------------
