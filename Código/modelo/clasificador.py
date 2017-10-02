# ----------------------------------------------------------------------------------------------------------------------

from coleccion import *
from entrenamiento import *

# ----------------------------------------------------------------------------------------------------------------------


class Clasificador(object):

    def __init__(self, entrenamiento, porcentaje_aceptacion):

        """
        Clase encargada de clasificar las imágenes desconocidas. Por defecto se basa en la distancia euclidiana para
        encontrar la muestra con la que más se parece la imagen desconocida. Para instanciar esta clase es necesario
        especificar los resultados del entrenamiento y fijar un minímo de aceptación para decidir si la imagen esta
        dentro del espacio creado
        @param entrenamiento: Instancia de Entrenamiento ejecutada con anterioridad
        @param porcentaje_aceptacion: Número ara decidir si la imagen es lo suficientemente parecida a una de las img
        """

        self.autoespacio = entrenamiento.autoespacio
        self.proyecciones = entrenamiento.proyecciones
        self.muestra_promedio = entrenamiento.muestra_promedio
        self.indice_aceptacion = porcentaje_aceptacion / 100

    # ------------------------------------------------------------------------------------------------------------------

    def clasificar(self, img):

        """
        Con base al modelo de clasificación planteado, se clasifica la imagen desconocida retornando un índice con el
        que se podrá consultar a la colección la etiqueta (o ruta) del sujeto. El grado de similitud se obtiene con base
        a la imagen más distante a la imagen desconocida, siendo esta 0
        @param img: imagen obtenida por cv.imread o ruta de la imagen
        @return: Tupla (I, S), donde I es el indíce de la imagen más parecida(número de imagen en la matriz de muestras)
        y S es la similitud obtenida (de 0 a 1). Retorna como I = -1 si la imagen no se encuentra dentro del autoespacio
        """

        # Abrimos la imagen si recibimos la ruta
        img = cv.imread(img, 0) if type(img) == str else img

        # Se convierte la imagen de 2D a 1D y se centra con base al origen
        img = np.matrix(img, dtype="float64").flatten().T
        img -= self.muestra_promedio

        # Se obtiene la proyeccion (calculo de pesos)
        img_proyectada = self.autoespacio.T * img

        # Distancia euclidiana
        distancias = self.proyecciones - img_proyectada
        distancias = np.linalg.norm(distancias, axis=0)

        # Calculando el índice de similitud con base al la imagen más distante (índice 0)
        similitudes = np.abs((distancias / np.max(distancias)) - 1)

        # Obtenemos el indice de la imagen y la mejor similitud
        similitud = np.max(similitudes)
        indice = np.argmax(similitudes)

        if similitud < self.indice_aceptacion:
            return -1, 0

        return indice, similitud

# ----------------------------------------------------------------------------------------------------------------------

    def leer_indexado(self, sufijo):

        """
        Lee los archivos indexados y los carga en memoria mediante objetos
        @param sufijo: sufijo con el que se guardaron los archivos indexados
        @return: tupla (objeto_coleccion, objeto_entrenamiento) con los valores asignados y listos para hacer una
        clasificador
        """

        prefijo = '..\\..\\Index\\'
        sufijo += '.txt'

        # Lectura del archivo que contiene la informacion de la coleccion
        f_coleccion = open(prefijo + 'coleccion_' + sufijo, 'r')
        dicc_coleccion = eval(f_coleccion.read())
        f_coleccion.close()

        # Construir objeto de coleccion
        coleccion = Coleccion(dicc_coleccion['ruta_datos'], dicc_coleccion['regex_sujs'], dicc_coleccion['regex_imgs'])
        coleccion.dic_imgs = dicc_coleccion['dic_imgs']
        coleccion.alto_img = dicc_coleccion['alto_imgs']
        coleccion.ancho_img = dicc_coleccion['ancho_imgs']
        coleccion.total_imgs = dicc_coleccion['total_imgs']
        coleccion.pixeles_img = dicc_coleccion['pixeles_img']

        # Construir objeto de entrenamiento
        entrenamiento = Entrenamiento
        entrenamiento.muestra_promedio = np.loadtxt(prefijo + 'muestra_promedio_' + sufijo, dtype='float64')
        entrenamiento.autoespacio = np.loadtxt(prefijo + 'autoespacio_' + sufijo, dtype='float64')
        entrenamiento.proyecciones = np.loadtxt(prefijo + 'proyecciones_' + sufijo, dtype='float64')

        return coleccion, entrenamiento

# ----------------------------------------------------------------------------------------------------------------------
