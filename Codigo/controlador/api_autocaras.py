# ----------------------------------------------------------------------------------------------------------------------

from controlador.controlador import *

# ----------------------------------------------------------------------------------------------------------------------


class APIAutocaras(object):

    def __init__(self):

        self.ctrl = Controlador()

    # ------------------------------------------------------------------------------------------------------------------

    def indexar_coleccion(self):

        """
        Indexa la colección de imagenes con base al archivo configuracion.py
        @return diccionario con información de la operación
        """

        try:

            self.ctrl.indexar_coleccion()

            return {"estado": "OK",
                    "mensaje": "La operación se ha realizado con exito"}

        except Exception as ex:

            return {"estado": "ERROR",
                    "mensaje": "La operación ha fallado",
                    "detalles": str(getattr(ex, 'message', repr(ex))) }

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
                    "detalles": str(getattr(ex, 'message', repr(ex)))}

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
                    'ruta_img': str(img_similar),
                    'grado_similitud': str(similitud)}

        except Exception as ex:

            return {"estado": "ERROR",
                    "mensaje": "La operación ha fallado",
                    "detalles": getattr(ex, 'message', repr(ex))}

    # ------------------------------------------------------------------------------------------------------------------

    def ejecutar_evaluacion(self, ruta_archivo='AT&T'):

        """
        Crea un informe con la evaluación del sistema
        @param ruta_archivo: Ruta absoluta del archivo a crear para guardar el informe de la evaluación
        @return no retorna algun valor.
        """

        try:
            ruta_informe = self.ctrl.ejecutar_evaluacion(ruta_archivo)

            return {"estado": "OK",
                    "mensaje": "La operación se ha realizado con exito",
                    "ruta_informe": ruta_informe}
        
        except Exception as ex:

            return {"estado": "ERROR",
                    "mensaje": "La operación ha fallado",
                    "detalles": getattr(ex, 'message', repr(ex))}


# ----------------------------------------------------------------------------------------------------------------------
