# ----------------------------------------------------------------------------------------------------------------------

import os
import pip

# ----------------------------------------------------------------------------------------------------------------------


def instalar_dependencias():

    try:
        pip.main(["install", "numpy", "django", "opencv-python"])
    except OSError:
        print("No se han podido instalar las dependencias")
        print("Intente instalar manualmente con permisos de administrador: ")
        print("\n > pip install numpy django opencv-python")

# ----------------------------------------------------------------------------------------------------------------------


comando = "python manage.py runserver"
os.system(comando)
# exec(open("./manage.py").read())

# ----------------------------------------------------------------------------------------------------------------------
