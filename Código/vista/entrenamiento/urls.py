from django.conf.urls import url

from . import views

app_name = 'entrenamiento'
urlpatterns = [
    # ex: /entrenamiento/
    url(r'^$', views.index, name='index'),
]