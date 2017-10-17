# ----------------------------------------------------------------------------------------------------------------------

import os
import time
import webbrowser
import threading
from instalador import *

# ----------------------------------------------------------------------------------------------------------------------


def iniciar_servidor():

    print("Inicializando servidor...")

    # Pedimos al SO que ejecute inicialice el servidor en el puerto 9000
    threading.Thread(target=abrir_pagina_web).start()
    os.system("python vista/manage.py runserver 9000")

# ----------------------------------------------------------------------------------------------------------------------


def abrir_pagina_web():

    print("Abriendo página web...")

    # Esperamos 2 segundos a que se inicialice el servidor
    time.sleep(2)
    webbrowser.open("http://localhost:9000/autoCaras/")

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    print("Espere porfavor... ")

    if verificar_permisos():
        instalar_dependencias()
    else:
        # Sino tiene permisos trata de darlos
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "instalador.py", None, 1)

    iniciar_servidor()

# ----------------------------------------------------------------------------------------------------------------------
