# ----------------------------------------------------------------------------------------------------------------------

from modelo.coleccion import *


# ----------------------------------------------------------------------------------------------------------------------


class Clasificador(object):

    def __init__(self, coleccion, entrenamiento, porcentaje_aceptacion):

        """
        Clase encargada de clasificar las imágenes desconocidas. Por defecto se basa en la distancia euclidiana para
        encontrar la muestra con la que más se parece la imagen desconocida. Para instanciar esta clase es necesario
        especificar los resultados del entrenamiento y fijar un minímo de aceptación para decidir si la imagen esta
        dentro del espacio creado
        @param coleccion: Instacia de Coleccion
        @param entrenamiento: Instancia de Entrenamiento ejecutada con anterioridad
        @param porcentaje_aceptacion: Número ara decidir si la imagen es lo suficientemente parecida a una de las img
        """

        self.coleccion = coleccion
        self.entrenamiento = entrenamiento
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
        @return: ruta_sujeto, ruta_img_encontrada, similitud
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

        # Si la similitud es menor al minimo quiere decir que el sujeto no se reconoce en la BD
        if similitud < self.indice_aceptacion:
            return Configuracion.SUJ_DESCONOCIDO, Configuracion.IMG_DESCONOCIDA, similitud

        # Consultamos a que sujeto pertenece el indice que obtuvimos
        indice = self.entrenamiento.indices_entrenamiento[indice]
        consulta = self.coleccion.consultar_img(indice)
        ruta_sujeto = consulta[0]
        ruta_img = consulta[1]

        return ruta_sujeto, ruta_img, similitud

# ----------------------------------------------------------------------------------------------------------------------
