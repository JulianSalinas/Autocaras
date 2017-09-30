# ----------------------------------------------------------------------------------------------------------------------

import numpy as np

# ----------------------------------------------------------------------------------------------------------------------

# TODO, no se esta usando el mínimo de aceptación todavía


class Clasificacion(object):

    def __init__(self, entrenamiento, indice_aceptacion):

        """
        Clase encargada de clasificar las imágenes desconocidas. Por defecto se basa en la distancia euclidiana para
        encontrar la muestra con la que más se parece la imagen desconocida. Para instanciar esta clase es necesario
        especificar los resultados del entrenamiento y fijar un minímo de aceptación para decidir si la imagen esta dentro
        del espacio creado.
        @param entrenamiento: Instancia de Entrenamiento ejecutada con anterioridad
        @param indice_aceptacion: Índice para decidir si la imagen es lo suficientemente parecida a una de las img
        """

        self.autoespacio = entrenamiento.autoespacio
        self.proyecciones = entrenamiento.proyecciones
        self.muestra_promedio = entrenamiento.muestra_promedio
        self.indice_aceptacion = indice_aceptacion

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar(self, img_desconocida):

        """
        Con base al modelo de clasificación planteado, se busca el índice del sujeto más parecido. El grado de similitud
        se obtiene con base a la imagen más distante de la imagen desconocida, siendo esta similitud 0
        @param img_desconocida: obtenido por cv.imread
        @return: Tupla (I, S), donde I es el indíce de la imagen más parecida(número de imagen en la matriz de muestras)
        y S es la similitud obtenida (de 0 a 1)
        """

        # Se convierte la imagen de 2D a 1D y se centra con base al origen
        img = np.matrix(img_desconocida, dtype="float64").flatten().T
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
            raise Exception("El sujeto no se encuentra definido")

        return indice, similitud

# ----------------------------------------------------------------------------------------------------------------------
