from __future__ import unicode_literals

from django.shortcuts import render

from .forms import FormularioReconocimiento
from .models import Integrante

from fachada_autocaras import *
api = FachadaAutocaras()

"""
***********************************************************************
Vista para cargar la seccion de reconocimiento del sistema
***********************************************************************
"""
def reconocimiento(request):

    form = FormularioReconocimiento(request.POST or None, request.FILES or None)
    if form.is_valid():
        imagen = form.save(commit=False)
        imagen.file = request.FILES['file']
        imagen.save()
        print(imagen.file.url)

        ruta_img = imagen.file.url
        ruta_img = "../vista" + ruta_img
        sujeto_identificado, img_similar, grado_similitud, ruta_img = api.ejecutar_clasificacion(ruta_img)

        return render(request, 'app/reconocimientoRes.html', {'ruta_img': str(ruta_img), 'sujeto_identificado':str(sujeto_identificado), 'img_similar':str(img_similar), 'grado_similitud':str(grado_similitud)})

    context = {
        'form': form,
    }
    return render(request, 'app/reconocimiento.html', context)





"""
***********************************************************************
Vista para cargar los datos del entrenamiento
***********************************************************************
"""
def entrenamiento(request):
    if(request.method == 'POST'):
        valPorColeccion = request.POST.get('valPorColeccion',"")
        valPorValores = request.POST.get('valPorValores',"")
        valPorAceptacion = request.POST.get('valPorAceptacion',"")
        print("Valores: ")
        print(str(valPorAceptacion))
        print(valPorColeccion)
        print(valPorValores)

        return render(request, 'app/entrenamientoRes.html',{})

    return render(request, 'app/entrenamiento.html', {})






"""
***********************************************************************
Vista para controlar la seccion AcercaDe que contiene
los datos del proyecto y los integrantes
***********************************************************************
"""
def acercaDe(request):
    integrantes = Integrante.objects.all()
    context = {'integrantes': integrantes}
    return render(request, 'app/acercaDe.html', context)
