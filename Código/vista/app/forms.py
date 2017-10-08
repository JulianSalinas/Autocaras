from django import forms

from .models import FileField


class FormularioReconocimiento(forms.ModelForm):

    class Meta:
        model = FileField
        fields = ['file']

