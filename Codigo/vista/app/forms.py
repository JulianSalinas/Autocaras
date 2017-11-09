from django import forms

from .models import FileField

"""
@author Julian Salinas, Armando Lopez, Andrey Mendoza, Brandon Dinarte
@version 1.6.49
"""

class FormularioReconocimiento(forms.ModelForm):

    class Meta:
        model = FileField
        fields = ['file']

