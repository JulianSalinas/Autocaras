from django.conf.urls import url

from . import views


app_name = 'reconocimiento'
urlpatterns = [
    # ex: /reconocimiento/
    url(r'^$', views.index, name='index'),
    # ex: /recococimiento/5/
    url(r'^res/$', views.res, name='res'),
]
