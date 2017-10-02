# ----------------------------------------------------------------------------------------------------------------------

from clasificador import *
from evaluacion import *
from dao_indice import *

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

        # TODO Aquí se deberían cargar las clases guardadas

        self.dao_indices = DaoIndices()

        # Para utilizar el indexado generado anteriormente
        self.coleccion, self.entrenamiento = self.dao_indices.leer_indexado('AT&T')
        self.clasificador = Clasificador(self.entrenamiento, 75)

        # Para indexar y utilizar este mismo indexado en memoria
        # self.coleccion = None
        # self.entrenamiento = None
        # self.clasificador = None

    # ------------------------------------------------------------------------------------------------------------------

    def indexar_coleccion(self, ruta_datos="..\\..\\Datos", regex_sujs="s[0-9]*", regex_imgs="\\[0-9]*.pgm"):

        """
        Indexa la colección de imagenes que se encuentre en una ruta dada
        @param ruta_datos: Ruta donde estan las imagenes
        @param regex_sujs: Expresión regula que indique que carpetas corresponden a sujetos
        @param regex_imgs: Expresión regula que indique archivos corresponden a la imagen de un sujeto
        @return self.coleccion
        """

        self.coleccion = Coleccion(ruta_datos, regex_sujs, regex_imgs)
        self.dao_indices.guardar_coleccion('AT&T', self.coleccion)
        return self.coleccion

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_entrenamiento(self, porcentaje_coleccion=100, porcentaje_valores=85, porcentaje_aceptacion=75):

        """
        Ejecuta el entrenamiento del sistema
        @param porcentaje_coleccion: Porcentaje de la colección que se usará para realizar el entrenamiento
        @param porcentaje_valores: Porcentaje de valores (autocaras o componentes) que se desean conservar
        @param porcentaje_aceptacion: Procentaje de aceptación mínimo para que el clasificador reconozca que una imagen
        desconocida se encuentra dentro del autoespacio
        @return self.entrenamiento, self.clasificador
        """

        total_sujs = self.coleccion.total_sujs
        imgs_x_suj = self.coleccion.total_imgs // total_sujs
        cant_imgs = int(imgs_x_suj * porcentaje_coleccion / 100)
        indices_subconjunto = np.array([], dtype="int32")

        # Obtenemos los índices de las imagenes que vamos a usar
        for i in range(0, total_sujs):
            escogidos = np.random.choice(range(0, imgs_x_suj), cant_imgs, False)
            escogidos += i * imgs_x_suj
            escogidos = np.sort(escogidos)
            indices_subconjunto = np.append(indices_subconjunto, [escogidos])

        # Se obtiene el subconjunto de entrenamiento y se entrena el sistema
        subconjuto = self.coleccion.obt_subconjunto(indices_subconjunto)
        subconjuto_entrenamiento = subconjuto, indices_subconjunto
        self.entrenamiento = Entrenamiento(subconjuto_entrenamiento, porcentaje_valores)
        self.clasificador = Clasificador(self.entrenamiento, porcentaje_aceptacion)

        # Indexa los archivos para clasificaciones futuras
        self.dao_indices.guardar_entrenamiento('AT&T', self.entrenamiento)

        return self.entrenamiento, self.clasificador

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_clasificacion(self, img):

        """
        Ejecuta la clasificación para una imagen mediante el método del centroide más cercano
        @param img: imagen o ruta de la imagen desconocida que se desea clasificar
        @return: ruta_sujeto, ruta_img, similitud
        """

        img = cv.imread(img, 0) if type(img) == str else img

        if img is not None:
            indice, similitud = self.clasificador.clasificar(img)
            ruta_suj, ruta_img = self.coleccion.consultar_img(indice)
            return ruta_suj, ruta_img, similitud

        raise IOError

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_evaluacion(self):

        """
        Ejecuta la evaluación del sistema con base al último entrenamiento realizado. De la evaluación se puede extraer
        la tabla de imagenes clasificadas vs reales, la tabla de evaluaciones (vp, fp, vn, fn, tvp, tpp) y los promedios
        de dicha tabla de evaluaciónes.
        @return instacia de la clase Evaluación
        """

        return Evaluacion(self.coleccion, self.entrenamiento, self.clasificador)

# ----------------------------------------------------------------------------------------------------------------------
