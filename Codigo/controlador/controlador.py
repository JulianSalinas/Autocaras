# ----------------------------------------------------------------------------------------------------------------------

import pickle

from controlador.dao_evaluacion import *
from modelo.clasificador import *
from modelo.entrenamiento import *
from modelo.evaluacion import *
from modelo.utilitarios.conversor import *


# ----------------------------------------------------------------------------------------------------------------------

"""
@author Julian Salinas, Armando Lopez, Andrey Mendoza, Brandon Dinarte
@version 1.6.49
"""

class Controlador(object):

    def __init__(self):

        """
        Clase principal del sistema, aquí se reunen los casos de uso, como por ejemplo, entrenar el sistema, realizar
        la clasificación de imagenes desconocidas. Se debe tomar en cuenta las siguientes consideraciones:
            1. Indexar la colección de imágenes implica tener que re-entrenar el sistema
            2. Entrenar el sistema requiere refrescar el modelo para clasificación
            3. Antes de usar el modelo de clasificación el sistema debe de haber sido entrenado previamente
            4. Antes de evaluar al sistema se tiene que haber indexado la colección de imagenes
        @param Sin parametros
        @return Sin retorno
        """

        if not os.path.exists(Configuracion.RUTA_INDICE):
            os.makedirs(Configuracion.RUTA_INDICE)

        try:
            self.coleccion = pickle.load(open(Configuracion.RUTA_COLECCION, "rb"))
            self.entrenamiento = pickle.load(open(Configuracion.RUTA_ENTRENAMIENTO, "rb"))

        except FileNotFoundError or IOError:
            self.indexar_coleccion()
            self.ejecutar_entrenamiento()

        self.clasificador = Clasificador(self.entrenamiento, 75)

    # ------------------------------------------------------------------------------------------------------------------

    def indexar_coleccion(self, ruta_datos=None):

        """
        Indexa la colección de imagenes con base a las rutas del módulo configuración
        @param ruta_datos: ruta donde se encuentran las imagenes. Si no se especifica se tomará la ruta por defecto
        presente en el archivo configuracion.py
        @return no retorna ningun valor
        """

        if ruta_datos is not None:
            if os.path.isdir(ruta_datos):
                Configuracion.RUTA_DATOS = ruta_datos
            else:
                raise Exception("Debe específicar el nombre de un directorio")

        self.coleccion = Coleccion()

        pickle.dump(self.coleccion, open(Configuracion.RUTA_COLECCION, "wb"))

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_entrenamiento(self, porcentaje_coleccion=80, porcentaje_valores=85, porcentaje_aceptacion=75):

        """
        Ejecuta el entrenamiento del sistema
        @param porcentaje_coleccion: Porcentaje de la colección que se usará para realizar el entrenamiento
        @param porcentaje_valores: Porcentaje de valores (autocaras o componentes) que se desean conservar
        @param porcentaje_aceptacion: Procentaje de aceptación mínimo para que el clasificador reconozca un sujeto
        @return no retorna ningun valor
        """

        if self.coleccion is None:
            self.indexar_coleccion()

        self.entrenamiento = Entrenamiento(self.coleccion, porcentaje_coleccion, porcentaje_valores)
        self.clasificador = Clasificador(self.entrenamiento, porcentaje_aceptacion)

        pickle.dump(self.entrenamiento, open(Configuracion.RUTA_ENTRENAMIENTO, "wb"))

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_clasificacion(self, ruta_img_buscada):

        """
        Ejecuta la clasificación para una imagen mediante el método del centroide más cercano
        @param ruta_img_buscada: ruta de la imagen desconocida que se desea clasificar
        @return: ruta_sujeto, ruta_img_encontrada, similitud
        """

        if self.entrenamiento is None:
            self.ejecutar_entrenamiento()

        img_buscada = cv.imread(ruta_img_buscada, 0)

        if img_buscada is not None:

            indice, similitud = self.clasificador.clasificar(img_buscada)

            if indice == -1:
                return Configuracion.SUJ_DESCONOCIDO, Configuracion.IMG_DESCONOCIDA, similitud

            # Consultamos a que sujeto pertenece el indice que obtuvimos
            indice = self.entrenamiento.indices_entrenamiento[indice]
            consulta = self.coleccion.consultar_img(indice)
            ruta_sujeto = consulta[0]
            ruta_img = consulta[1]

            return ruta_sujeto, ruta_img, similitud

        raise IOError

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_evaluacion(self, directorio=None):

        """
        Ejecuta la evaluación del sistema con base al último entrenamiento realizado. De la evaluación se puede extraer
        la tabla de imagenes clasificadas vs reales, la tabla de evaluaciones (vp, fp, vn, fn, tvp, tpp) y los promedios
        de dicha tabla de evaluaciónes.
        NOTA: Si en el último entrenamiento se usó el 100% de la colección, significa que no habrán imagenes disponibles
        para realizar la evaluación, por tanto, la tabla generada estará llena con ceros
        @param directorio: Ruta donde se guardarán las tablas generadas por la evaluacion
        @return directorio donde fue generado los informes de la evaluacion
        """

        if self.entrenamiento is None:
            self.ejecutar_entrenamiento(porcentaje_aceptacion=0)

        if directorio is None:
            directorio = Configuracion.RUTA_MEDIA

        evaluacion = Evaluacion(self.coleccion, self.entrenamiento, self.clasificador)
        DaoEvaluacion.guardar(evaluacion, directorio)
        return directorio

# ----------------------------------------------------------------------------------------------------------------------
