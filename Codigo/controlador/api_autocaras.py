# ----------------------------------------------------------------------------------------------------------------------

from controlador.controlador import *

# ----------------------------------------------------------------------------------------------------------------------


class APIAutocaras(object):

    def __init__(self):

        self.ctrl = Controlador()

    # ------------------------------------------------------------------------------------------------------------------

    def indexar_coleccion(self, ruta_datos=None):

        """
        Indexa la colección de imagenes
        @param ruta_datos: ruta donde se encuentran las imagenes. Si no se especifica se tomará la ruta por defecto
        presente en el archivo configuracion.py
        @return diccionario con información de la operación
        """

        try:

            self.ctrl.indexar_coleccion(ruta_datos)

            return {"estado": "OK",
                    "mensaje": "La operación se ha realizado con exito"}

        except Exception as ex:

            return {"estado": "ERROR",
                    "mensaje": "La operación de indexar ha fallado",
                    "detalles": str(getattr(ex, 'message', str(ex)))}

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_entrenamiento(self, porcentaje_coleccion=80, porcentaje_valores=85, porcentaje_aceptacion=75):

        """
        Ejecuta el entrenamiento del sistema
        @param porcentaje_coleccion: Porcentaje de la colección que se usará para realizar el entrenamiento
        @param porcentaje_valores: Porcentaje de valores (autocaras o componentes) que se desean conservar
        @param porcentaje_aceptacion: Procentaje de aceptación mínimo para que el clasificador reconozca un sujeto
        @return diccionario con información de la operación
        """

        try:
            self.ctrl.ejecutar_entrenamiento(porcentaje_coleccion, porcentaje_valores, porcentaje_aceptacion)

            return {"estado": "OK",
                    "mensaje": "La operación se ha realizado con exito"}

        except Exception as ex:

            return {"estado": "ERROR",
                    "mensaje": "La operación ha fallado",
                    "detalles": str(getattr(ex, 'message', str(ex)))}

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_clasificacion(self, ruta_img_buscada):

        """
        Ejecuta la clasificación para una imagen
        @param ruta_img_buscada: ruta de la imagen desconocida que se desea clasificar
        @return: diccionario con información de la operación y con los siguientes datos:
                 * sujeto_identificado
                 * img_similar
                 * grado_similitud
        """

        try:
            ruta_sujeto, img_similar, similitud = self.ctrl.ejecutar_clasificacion(ruta_img_buscada)

            return {'estado': "OK",
                    'mensaje': "La operación se ha realizado con exito",
                    'sujeto_identificado': str(ruta_sujeto),
                    'img_similar': str(img_similar),
                    'grado_similitud': str(similitud)}

        except Exception as ex:

            return {"estado": "ERROR",
                    "mensaje": "La operación ha fallado",
                    "detalles": getattr(ex, 'message', str(ex))}

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_evaluacion(self, directorio=None):

        """
        Crea archivos csv de la evaluación del sistema con base en el último entrenamiento realizado
        NOTA: Si en el último entrenamiento se usó el 100% de la colección, significa que no habrán imagenes disponibles
        para realizar la evaluación, por tanto, la tabla generada estará llena con ceros
        @param directorio: Ruta donde se guardarán las tablas generadas por la evaluacion
        @return diccionario con información de la operación, el diccionario contiene el directorio donde fueron
        generados los informes de la evaluacion
        """

        try:
            ruta_informes = self.ctrl.ejecutar_evaluacion(directorio)

            return {"estado": "OK",
                    "mensaje": "La operación se ha realizado con exito",
                    "ruta_informes": ruta_informes}
        
        except Exception as ex:

            return {"estado": "ERROR",
                    "mensaje": "La operación ha fallado",
                    "detalles": getattr(ex, 'message', str(ex))}


# ----------------------------------------------------------------------------------------------------------------------
