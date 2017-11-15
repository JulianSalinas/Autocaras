# ----------------------------------------------------------------------------------------------------------------------

import subprocess
from unittest import TestCase

from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from controlador.dao_evaluacion import *
from modelo.clasificador import *
from modelo.entrenamiento import *
from modelo.evaluacion import *


# ----------------------------------------------------------------------------------------------------------------------

"""
@author Julian Salinas, Armando Lopez, Andrey Mendoza, Brandon Dinarte
@version 1.6.49
"""


# Colocamos la configuracion para que la coleccion solo se tenga 4 sujetos
# Configuracion.REGEX_SUJS = "s[1-4]"
coleccion = Coleccion()


# Se usará un 50% de la colección (al azar) para evaluar el sistema. Se usará el 80% de autocaras
entrenamiento = Entrenamiento(coleccion, porcentaje_coleccion=50, porcentaje_valores=50)

# Ejecutamos la evaluación usando el entrenamiento previo. Se usa un indice de aceptacion de 0. para que todos
# los rostros sean considerados como que se encuentran dentro del autoespacio, es decir, aunque la entrada sea
# una imagen que no sea un rostro, de igual manera se tomará la más cercana
evaluacion = Evaluacion(coleccion, entrenamiento, Clasificador(entrenamiento, 0.0))

# Extraccion de las columnas necesarias
# VPR = np.array(evaluacion.tabla_evaluacion[:, evaluacion.Sensibilidad].T)[0]
# FPR = 1 - np.array(evaluacion.tabla_evaluacion[:, evaluacion.Especificidad].T)[0]
VPR = np.array([np.mean(np.array(evaluacion.tabla_evaluacion[:, evaluacion.Sensibilidad].T)[0])])
FPR = np.array([np.mean(1 - np.array(evaluacion.tabla_evaluacion[:, evaluacion.Especificidad].T)[0])])
orden = np.argsort(FPR)
VPR = VPR[orden]
FPR = FPR[orden]

# Se agregan los clasificadores por defecto
x = np.append(np.append([0], FPR), [1])
y = np.append(np.append([0], VPR), [1])
print(x)
print(y)

# fpr, tpr, thresholds = roc_curve(predictions_test, outcome_test)
roc_auc = auc(x, y)

# Mostramos la grafica
plt.figure()
plt.title("ROC (Receiver Operating Characteristic)")
plt.ylabel("True Positive Rate")
plt.xlabel("False Positive Rate")
plt.plot(x, y, color='darkorange', lw=1, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot(x, y,'or')
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.ylim([-0.05, 1.05])
plt.legend(loc="lower right")
plt.show()

# Se guardan las tablas generadas por la evaluación como archivos csv
DaoEvaluacion.guardar(evaluacion, Configuracion.RUTA_EVALUACION)

# Verificamos manualmente que los archivos existan y que no esten vacio viendo la carpeta
subprocess.call("explorer " + os.path.join(Configuracion.RUTA_MEDIA), shell=True)

# ----------------------------------------------------------------------------------------------------------------------

