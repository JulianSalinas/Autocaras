from django.conf.urls import url

from . import views

app_name = 'autoCaras'
urlpatterns = [
    # ex: /autoCaras/
    url(r'^$', views.reconocimiento, name='reconocimiento'),
    # ex: /autoCaras/reconocimiento/
    url(r'^reconocimiento$', views.reconocimiento, name='reconocimiento'),
    # ex: /autoCaras/acercaDe/
    url(r'^acercaDe$', views.acerca_de, name='acerca_de'),
    # ex: /autoCaras/entrenamiento/
    url(r'^entrenamiento$', views.entrenamiento, name='entrenamiento'),
    # ex: /autoCaras/evaluar/
    url(r'^evaluar$', views.evaluar, name='evaluar'),
]
