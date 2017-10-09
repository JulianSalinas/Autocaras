# ----------------------------------------------------------------------------------------------------------------------

import re

# ----------------------------------------------------------------------------------------------------------------------


class DaoEvaluacion:

    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def guardar(nombre_archivo, evaluacion):

        """
        Guarda los resultados de la evaluacion del sistema en un archivo en formato csv.
        @param nombre_archivo: nombre con el cual se va a guardar la evaluacion actual.
        @param evaluacion: objeto evaluacion con los valores calculados
        @return: no retorna algun valor.
        """

        tabla_evaluacion = evaluacion.agregar_encabezados()
        f_evaluacion = open(nombre_archivo + '.csv', 'w')

        fin_fila = 0
        for x in np.nditer(tabla_evaluacion):
            linea = str(x)

            # Extraer solamente el nombre de sujeto
            if fin_fila == 0:
                sujeto = re.findall(r's\d+', str(x))
                if len(sujeto) > 0:
                    linea = sujeto[0]

            # Verificar si es necesario el cambio de fila
            if fin_fila == 5:
                linea += '\n'
                fin_fila = 0
            else:
                linea += ','
                fin_fila += 1

            f_evaluacion.write(linea)
        f_evaluacion.close()

# ----------------------------------------------------------------------------------------------------------------------
