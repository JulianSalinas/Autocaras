from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Integrante

from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    integrantes = Integrante.objects.all()
    context = {'integrantes': integrantes}
    return render(request, 'acercaDe/index.html', context)

def detail(request, integrante_id):
    integrante = get_object_or_404(Integrante, pk=integrante_id)
    return render(request, 'acercaDe/detail.html', {'integrante': integrante})

def results(request, question_id):
    response = "Acerca de, You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Acerca de, You're voting on question %s." % question_id)