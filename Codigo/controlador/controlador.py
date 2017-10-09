# ----------------------------------------------------------------------------------------------------------------------

import pickle
from modelo.clasificador import *
from modelo.entrenamiento import *
from modelo.evaluacion import *
from modelo.utilitarios.conversor import *
from controlador.dao_evaluacion import *

# ----------------------------------------------------------------------------------------------------------------------


class Controlador(object):

    def __init__(self):

        """
        Clase principal del sistema, aquí se reunen los casos de uso, como por ejemplo, entrenar el sistema, realizar
        la clasificación de imagenes desconocidas. Se debe tomar en cuenta las siguientes consideraciones:
            1. Indexar la colección de imágenes implica tener que re-entrenar el sistema
            2. Entrenar el sistema requiere refrescar el modelo para clasificación
            3. Antes de usar el modelo de clasificación el sistema debe de haber sido entrenado previamente
            4. Antes de evaluar al sistema se tiene que haber indexado la colección de imagenes
        """

        if not os.path.exists(Configuracion.RUTA_INDICE):
            os.makedirs(Configuracion.RUTA_INDICE)

        try:
            self.coleccion = pickle.load(open(Configuracion.RUTA_COLECCION, "rb"))
            self.entrenamiento = pickle.load(open(Configuracion.RUTA_ENTRENAMIENTO, "rb"))

        except FileNotFoundError or IOError:
            self.indexar_coleccion()
            self.ejecutar_entrenamiento()

        self.clasificador = Clasificador(self.coleccion, self.entrenamiento, 75)

    # ------------------------------------------------------------------------------------------------------------------

    def indexar_coleccion(self):

        """
        Indexa la colección de imagenes con base a las rutas del módulo configuración
        @return no retorna ningun valor
        """

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
        self.clasificador = Clasificador(self.coleccion, self.entrenamiento, porcentaje_aceptacion)

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
            return self.clasificador.clasificar(img_buscada)

        raise IOError

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_evaluacion(self, nombre_archivo):

        """
        Ejecuta la evaluación del sistema con base al último entrenamiento realizado. De la evaluación se puede extraer
        la tabla de imagenes clasificadas vs reales, la tabla de evaluaciones (vp, fp, vn, fn, tvp, tpp) y los promedios
        de dicha tabla de evaluaciónes. El informe se guarda en un archivo
        NOTA: Si en el último entrenamiento se usó el 100% de la colección, significa que no habrán imagenes disponibles
        para realizar la evaluación, por tanto, la tabla generada estará llena con ceros
        @param nombre_archivo: Ruta absoluta del archivo a crear para guardar el informe de la evaluación
        @return instacia de la clase Evaluación
        """

        if self.entrenamiento is None:
            self.ejecutar_entrenamiento()

        dao = DaoEvaluacion()
        evaluacion = Evaluacion(self.coleccion, self.entrenamiento, self.clasificador)
        dao.guardar(nombre_archivo, evaluacion)
        return nombre_archivo

# ----------------------------------------------------------------------------------------------------------------------
