from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.core.urlresolvers import reverse

from django.template import loader
from django.http import HttpResponse

from django.db import models


from .forms import AlbumForm
from .models import Album


# Create your views here.

def index(request):
    form = AlbumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        album = form.save(commit=False)
        #album.user = request.user
        album.album_logo = request.FILES['album_logo']
        file_type = album.album_logo.url.split('.')[-1]
        file_type = file_type.lower()
        print(album.album_logo.url)
        album.save()
        #Ejecucion del reconocimiento
        result = "Este es el resultado del reconocimiento"
        
        return render(request, 'reconocimiento/detail.html', {'album': album, 'result':result})
    context = {
        'form': form,
    }
    return render(request, 'reconocimiento/index.html', context)


def res(request):
    
    response = "You're looking at the results of image."
    return HttpResponse(response)
