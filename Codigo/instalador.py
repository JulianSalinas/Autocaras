# ----------------------------------------------------------------------------------------------------------------------

import sys
import pip
import ctypes

# ----------------------------------------------------------------------------------------------------------------------


def verificar_permisos():

    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# ----------------------------------------------------------------------------------------------------------------------


def instalar_dependencias():

    try:
        print("Instalando numpy")
        pip.main(["install", "numpy"])
        print("Instalando django")
        pip.main(["install", "django"])
        print("Instalando pandas")
        pip.main(["install", "pandas"])
        print("Instalando opencv-python")
    except:
        error_dependencias()

# ----------------------------------------------------------------------------------------------------------------------


def error_dependencias():

    print("No se han podido instalar las dependencias")
    print("Intente instalar manualmente con permisos de administrador")
    input("\n > pip install numpy django opencv-python pandas")
    sys.exit(0)

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    
    if verificar_permisos():
        instalar_dependencias()
        print("Dependencias instaladas correctamente")
    else:

        # Sino tiene permisos trata de correr otra vez el programa con estos
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "instalador.py", None, 0)

# ----------------------------------------------------------------------------------------------------------------------
