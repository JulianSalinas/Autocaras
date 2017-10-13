## Ver versión:
	python -m django --version

## Instalar Django (1.11.5)
	pip install Django

## Iniciar un proyecto
	django-admin startproject AutoCaras

## Archivos importantes:
	manage.py: Una utilidad de la línea de comandos que le permite interactuar con este proyecto Django de diferentes formas. Puede leer todos los detalles sobre :archivo:`manage.py` en el :doc: :/ref/django-admin.

	En interior del directorio mysite/ es el propio paquete de Python para su proyecto. Su nombre es el nombre del paquete de Python que usted tendrá que utilizar para importar todo dentro de este (por ejemplo, mysite.urls).
		mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
		mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
		mysite/urls.py: Las declaraciones URL para este proyecto Django; una «tabla de contenidos» de su sitio basado en Django. Puede leer más sobre las URLs en URL dispatcher.
		mysite/wsgi.py: Un punto de entrada para que los servidores web compatibles con WSGI puedan servir su proyecto. Consulte :doc:`/howto/deployment/wsgi/index`para más detalles.

## Ejecutar servidor:
	> python manage.py runserver

## Ejecutar especificando el puerto:
	 > python manage.py runserver 8080

## Recarga Automática:
	El servidor de desarrollo recarga de forma automática el código Python para cada petición cuando sea necesario. No es necesario reiniciar el servidor para que los cambios de código surtan efecto. Sin embargo, algunas acciones como la adición de archivos no provoca un reinicio, por lo que tendrá que reiniciar el servidor en estos casos.

## Crear aplicación:
	python manage.py startapp NOMBRE

## Migrar la BD:
	python manage.py migrate

## Pasos para efectuar cambios en los modelos
	* Cambie sus modelos (en models.py).
	* Ejecute el comando python manage.py makemigrations NombreAplicacion para crear migraciones para esos cambios
	* Ejecute el comando python manage.py migrate para aplicar esos cambios a la base de datos.

## Crear SuperUsuario
	python manage.py createsuperuser

## Direcciones válidas de la página web

	# ex: /autoCaras/

	# ex: /autoCaras/reconocimiento/

    	# ex: /autoCaras/acercaDe/

    	# ex: /autoCaras/entrenamiento/

    	# ex: /autoCaras/evaluar/
    url(r'^evaluar$', views.evaluar, name='evaluar'),
