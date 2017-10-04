from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404


from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {}
    return render(request, 'reconocimiento/index.html', context)

def detail(request, question_id):
    return HttpResponse("Viendo el detalle de reconocimiento")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)