# ----------------------------------------------------------------------------------------------------------------------

import os
import pip

# ----------------------------------------------------------------------------------------------------------------------


def instalar_dependencias():

    try:
        pip.main(["install", "numpy", "django", "pandas", "opencv-python"])
    except OSError:
        print("No se han podido instalar las dependencias")
        print("Intente instalar manualmente con permisos de administrador: ")
        print("\n > pip install numpy django opencv-python")

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    instalar_dependencias()
    comando = "python vista/manage.py runserver 9000"
    os.system(comando)

# ----------------------------------------------------------------------------------------------------------------------
