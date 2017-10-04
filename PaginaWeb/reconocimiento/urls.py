from django.conf.urls import url

from . import views

app_name = 'reconocimiento'
urlpatterns = [
    # ex: /reconocimiento/
    url(r'^$', views.index, name='index'),
    # ex: /recococimiento/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /reconocimiento/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /reconocimiento/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]