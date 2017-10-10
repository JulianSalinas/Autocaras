
from __future__ import unicode_literals

from django.contrib import admin


# Registro de modelos para ser accedidos desde la base de datos
from .models import Integrante
admin.site.register(Integrante)
