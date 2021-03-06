# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

"""
@author Julian Salinas, Armando Lopez, Andrey Mendoza, Brandon Dinarte
@version 1.6.49
"""

@python_2_unicode_compatible  # only if you need to support Python 2
class Integrante(models.Model):
    nombre = models.CharField(max_length=200)
    carnet = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre+' - '+self.carnet

    
    
class FileField(models.Model):
    file = models.FileField()