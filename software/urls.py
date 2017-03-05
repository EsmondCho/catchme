from django.conf.urls import url

from .views import *

urlpatterns = [

    url(r'^$', introduction, name='introduction'),

    url(r'^mypocket$', mypocket, name='mypocket'),

    url(r'^catchsenior$', catchsenior, name='catchsenior'),

    url(r'^recognize$', recognize, name='recognize'),

    url(r'^rank/freshman$', rank_freshman, name='rank_freshman'),
    url(r'^rank/senior$', rank_senior, name='rank_senior'),

    url(r'^senior/(?P<pk>[0-9]+)/$', senior, name='senior'),
    url(r'^seniors$', seniors, name='seniors'),
    url(r'^seniors_search$', seniors_search, name='seniors_search'),

    url(r'^training$', training, name='training'),
    url(r'^training_result$', training_result, name='training_result'),

    url(r'^chatting$', chatting, name='chatting')

]
