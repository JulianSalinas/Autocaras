from django import forms
from django.contrib.auth.models import User

from .models import Album


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['album_logo']

