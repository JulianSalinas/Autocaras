from django.conf.urls import url

from . import views

app_name = 'acercaDe'
urlpatterns = [
    # ex: /acercaDe/
    url(r'^$', views.index, name='index'),
    # ex: /acercaDe/5/
    url(r'^(?P<integrante_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /acercaDe/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /acercaDe/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]