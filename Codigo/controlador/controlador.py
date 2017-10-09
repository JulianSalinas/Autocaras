# ----------------------------------------------------------------------------------------------------------------------

from modelo.utilitarios.conversor import *
from controlador.dao_indice import *
from modelo.entrenamiento import *
from modelo.clasificador import *
from modelo.evaluacion import *

# ----------------------------------------------------------------------------------------------------------------------


class Controlador(object):

    def __init__(self):

        # Utilizar el último entrenamiento ejecutado

        try:
            self.dao_indices = DaoIndice()
            self.coleccion = self.dao_indices.cargar_ultima_coleccion()
            self.entrenamiento = self.dao_indices.cargar_ultimo_entrenamiento()

        except FileNotFoundError or IOError:
            self.indexar_coleccion()
            self.ejecutar_entrenamiento()

        self.clasificador = Clasificador(self.coleccion, self.entrenamiento, 75)

    # ------------------------------------------------------------------------------------------------------------------

    def indexar_coleccion(self):

        """
        Indexa la colección de imagenes con base al modulo configuración
        """

        self.coleccion = Coleccion()
        self.dao_indices.guardar_coleccion(self.coleccion)
        return self.coleccion

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_entrenamiento(self, porcentaje_coleccion=80, porcentaje_valores=85, porcentaje_aceptacion=75):

        """
        Ejecuta el entrenamiento del sistema
        @param porcentaje_coleccion: Porcentaje de la colección que se usará para realizar el entrenamiento
        @param porcentaje_valores: Porcentaje de valores (autocaras o componentes) que se desean conservar
        @param porcentaje_aceptacion: Procentaje de aceptación mínimo para que el clasificador reconozca que una imagen
        desconocida se encuentra dentro del autoespacio
        @return self.entrenamiento, self.clasificador
        """

        if self.coleccion is None:
            self.indexar_coleccion()

        self.entrenamiento = Entrenamiento(self.coleccion, porcentaje_coleccion, porcentaje_valores)
        self.clasificador = Clasificador(self.coleccion, self.entrenamiento, porcentaje_aceptacion)

        # Indexa los indice para clasificaciones futuras
        self.dao_indices.guardar_entrenamiento(self.entrenamiento)

        return self.entrenamiento, self.clasificador

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

    def ejecutar_evaluacion(self, nombre_archivo='AT&T'):

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
            self.ejecutar_entrenamiento(porcentaje_coleccion=80)

        evaluacion = Evaluacion(self.coleccion, self.entrenamiento, self.clasificador)
        self.dao_indices.guardar_evaluacion(nombre_archivo, evaluacion)
        return evaluacion

# ----------------------------------------------------------------------------------------------------------------------
