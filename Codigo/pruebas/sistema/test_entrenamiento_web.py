# ----------------------------------------------------------------------------------------------------------------------

from unittest import TestCase
from selenium import webdriver

# ----------------------------------------------------------------------------------------------------------------------

"""
@author Julian Salinas, Armando Lopez, Andrey Mendoza, Brandon Dinarte
@version 1.6.49
"""

class TestEntrenamientoWeb(TestCase):

    """
    Clase encargada de probar el entrenamiento realizado desde la pagina web.
    """

    # ------------------------------------------------------------------------------------------------------------------

    def test_entrenamiento_web(self):

        """
        Entradas: Coleccion por defecto ofrecida desde la pagina web.
        Resultado esperado: La página a la cual se redirecciona luego del entrenamiento, debe contener el texto
        'La operacion se ha realizado con éxito'.
        @param Sin parametros
        @return Sin retorno
        """

        # Se crea la instancia del navegador
        navegador = webdriver.Firefox()
        navegador.get('http://localhost:9000/autoCaras/entrenamiento')

        # Se desmarca el chekcbox de utilizar nueva base de datos
        navegador.find_element_by_name('checkboxIndexar_lbl').click()

        # Se presiona el botón de 'Ejecutar' para solicitar el entrenamiento
        navegador.find_element_by_name('botonEjecutar').click()

        # Se verifica que el mensaje de éxito se encuentre en la página redireccionada
        assert 'La operación se ha realizado con éxito' in navegador.page_source

        # Cierre del navegador inicializado para la prueba
        navegador.quit()

    # ------------------------------------------------------------------------------------------------------------------
