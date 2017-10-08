from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from .forms import AlbumForm

from fachada_autocaras import *

api = FachadaAutocaras()


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

        ruta_img = album.album_logo.url
        ruta_img = "../vista" + ruta_img
        result = str(api.ejecutar_clasificacion(ruta_img))

        # result = test1.ejemplo(ruta_img)
        return render(request, 'reconocimiento/detail.html', {'album': album, 'result':result})

    context = {
        'form': form,
    }
    return render(request, 'reconocimiento/index.html', context)


def res(request):
    
    response = "You're looking at the results of image."
    return HttpResponse(response)
