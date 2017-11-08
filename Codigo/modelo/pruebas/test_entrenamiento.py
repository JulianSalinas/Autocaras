# ----------------------------------------------------------------------------------------------------------------------

from unittest import TestCase

from modelo.coleccion import *
from modelo.entrenamiento import *


# ----------------------------------------------------------------------------------------------------------------------


class TestEntrenamiento(TestCase):

    """
    Clase encargada de probar funciones y fragmentos importantes de código para el modulo modelo.entrenamiento
    """

    # ------------------------------------------------------------------------------------------------------------------

    def test_obt_indices_entrenamiento(self):

        """
        @author Julian Salinas, Andrey Mendoza, Armando Lopez, Brandon Dinarte
        @version 1.6.49
        Entradas: Coleccion y el porcentaje de la coleccion que vamos a utilizar para el entrenamiento
        Resultado esperado: Lista de indices que representan una imagen dentro de la coleccion. Se debe haber tomado
        igual cantidad de imagenes para cada sujeto
        @param sin parametros
        @return sin retorno
        """

        # Se crea una coleccion ficticia
        coleccion = Coleccion
        coleccion.dic_imgs = {
            0: ("suj1", "img1"),
            1: ("suj1", "img2"),
            2: ("suj2", "img1"),
            3: ("suj2", "img2"),
        }
        coleccion.total_sujs = 2
        coleccion.total_imgs = 4

        # Se crea una instancia de Entrenamiento para probar el método
        # Se usará un 50% de la coleccion, por tanto, se debe obtener 2 indices, es decir,
        # dos indices que representen dos imagenes, una para cada uno de los sujetos
        entrenamiento = object.__new__(Entrenamiento)
        entrenamiento.obt_indices_entrenamiento(coleccion, 70)

        # La cantidad de indices debe ser 2
        self.assertTrue(len(entrenamiento.indices_entrenamiento) == 2)

        # Las imagenes que representan dichos indices deben ser 1 para el suj1 y 1 para el suj2
        img_1 = entrenamiento.indices_entrenamiento[0]
        img_2 = entrenamiento.indices_entrenamiento[1]
        self.assertTrue(coleccion.dic_imgs[img_1][0] == "suj1")
        self.assertTrue(coleccion.dic_imgs[img_2][0] == "suj2")

    # ------------------------------------------------------------------------------------------------------------------

    def test_obt_promedio_muestras(self):

        """
        @author Julian Salinas, Andrey Mendoza, Armando Lopez, Brandon Dinarte
        @version 1.6.49
        Entradas: Matriz de muestras
        Resultado esperado: Al restar el promedio a la matriz, la sumatoria de todas las columnas debe ser 0
        @param sin parametros
        @return sin retorno
        """

        # Creamos una matriz de muestras ficticia
        mat_muestras = np.matrix([[30, 50],
                                  [10, 9.]], "float64")

        # Comprobando matriz de muestras con base al origen
        # Si la imagen esta centrada con base al origen, su sumatoria es 0
        muestra_promedio = np.mean(mat_muestras, axis=1, dtype="float64")
        mat_muestras -= muestra_promedio
        self.assertEqual(np.sum(mat_muestras), 0)

    # ------------------------------------------------------------------------------------------------------------------

    def test_mat_covarianza(self):

        """
        @author Julian Salinas, Andrey Mendoza, Armando Lopez, Brandon Dinarte
        @version 1.6.49
        Entradas: Matriz de muestras
        Resultado esperado: La matriz de covarianza debe coincidir con la matriz de covarianza que fue calculada
        anteriormente de formma manual
        @param sin parametros
        @return sin retorno
        """

        # Creamos una matriz de muestras ficticia
        mat_muestras = np.matrix([[4, 5],
                                  [1, 6]], "float64")

        # No es estrictamente la matriz de covarianza pues se usa un truco algebraico posterimente
        mat_covarianza = mat_muestras.T * mat_muestras
        mat_covarianza /= mat_muestras.shape[1] - 1

        # La matriz de obtenida debe ser la siguiente
        mat_covarianza_real = np.matrix([[17., 26.],
                                         [26., 61.]])

        self.assertTrue(np.allclose(mat_covarianza, mat_covarianza_real))

    # ------------------------------------------------------------------------------------------------------------------

    def test_autovects(self):

        """
        @author Julian Salinas, Andrey Mendoza, Armando Lopez, Brandon Dinarte
        @version 1.6.49
        Entradas: Matriz de covarianza
        Resultado esperado: Los autovectores/valores deben coincidir con los resultados tomados con la
        herramienta http://www.arndt-bruenner.de/mathe/scripts/engl_eigenwert2.htm
        @param sin parametros
        @return sin retorno
        """

        mat_cov = np.matrix([[4, 5],
                             [1, 6]], "float64")

        # Fragmento de código en la clase entrenamiento para obtener los autovectores/valores
        autovals, autovects = np.linalg.eig(mat_cov)
        orden = np.argsort(autovals)[::-1]
        autovals = autovals[orden]
        autovects = autovects[:, orden]

        # Revisamos que los autovalores/vectores coincidan
        autovals_reales = np.array([7.44948974278, 2.55051025721])
        autovects_reales = np.array([[-0.82311937947, -0.960455354058],
                                     [-0.567868371314, 0.278434036821]])

        self.assertTrue(np.allclose(autovals, autovals_reales))
        self.assertTrue(np.allclose(autovects, autovects_reales))

    def test_autoespacio(self):

        """
        @author Julian Salinas, Andrey Mendoza, Armando Lopez, Brandon Dinarte
        @version 1.6.49
        @param sin parametros
        @return sin retorno
        Entradas: Matriz de muestras y los autovectores
        Resultado esperado: El autoespacio conformado por los autovectores debe coincidir con el obtenido manualmente
        """

        # Creamos una matriz de muestras ficticia
        mat_muestras = np.matrix([[1, 2],
                                  [3, 0]], "float64")

        # Creamos los autovectores. Cabe destacar que no son los autovectores reales para la matriz de covariza que se
        # obtiene a partir de la matriz de muestras, sin embargo, no es necesario para esta prueba pues el objetivo es
        # saber que los calculos se están realizando correctamente
        autovects = np.matrix([[4, 4],
                               [2, 2]], "float64")

        autoespacio = mat_muestras * autovects.T
        autoespacio /= np.linalg.norm(autoespacio, axis=0)

        # Comparamos que el resultado obtenido sea igual a este siguiente
        val = 0.70710678
        autoespacio_real = np.array([[val, val],
                                     [val, val]], "float64")

        self.assertTrue(np.allclose(autoespacio, autoespacio_real))

# ----------------------------------------------------------------------------------------------------------------------

