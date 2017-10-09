from django.conf.urls import url

from . import views

app_name = 'autoCaras'
urlpatterns = [
    # ex: /AutoCaras/
    url(r'^$', views.reconocimiento, name='reconocimiento'),
    # ex: /AutoCaras/reconocimiento/
    url(r'^reconocimiento$', views.reconocimiento, name='reconocimiento'),
    # ex: /AutoCaras/acercaDe/
    url(r'^acercaDe$', views.acercaDe, name='acercaDe'),
    # ex: /AutoCaras/entrenamiento/
    url(r'^entrenamiento$', views.entrenamiento, name='entrenamiento'),
]
