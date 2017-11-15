# ----------------------------------------------------------------------------------------------------------------------

from unittest import TestCase
from selenium import webdriver
import os

# ----------------------------------------------------------------------------------------------------------------------

"""
@author Julian Salinas, Armando Lopez, Andrey Mendoza, Brandon Dinarte
@version 1.6.49
"""

class TestReconocimientoWeb(TestCase):

    """
    Clase encargada de probar el reconocimiento realizado desde la pagina web.
    """

    # ------------------------------------------------------------------------------------------------------------------

    def test_reconocimiento_web(self):

        """
        Entradas: Imagen de prueba.
        Resultado esperado: La página a la cual se redirecciona luego del entrenamiento, debe contener el texto
        'La operacion se ha realizado con éxito'.
        @param Sin parametros
        @return Sin retorno
        """

        # Se crea la instancia del navegador
        navegador = webdriver.Firefox()
        navegador.get('http://localhost:9000/autoCaras/reconocimiento')

        # Se presiona el botón de navegar archivos y se selecciona la imagen de prueba.
        navegador.find_element_by_name('file').send_keys(os.getcwd() + '\\datos_prueba\\sujeto_1_imagen_1.pgm')

        # Se presiona el botón de 'Ejecutar' para solicitar el reconocimiento
        navegador.find_element_by_name('botonEjecutar').click()

        # Se verifica que el mensaje de éxito se encuentre en la página redireccionada
        assert 'La operación se ha realizado con éxito' in navegador.page_source

        # Cierre del navegador inicializado para la prueba
        navegador.quit()

    # ------------------------------------------------------------------------------------------------------------------
