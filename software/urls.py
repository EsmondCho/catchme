from django.conf.urls import url

from .views import *

urlpatterns = [

    url(r'^$', introduction, name='introduction'),

    url(r'^mypockets/(?P<pk>[0-9]+)$', mypocket, name='mypocket'),
    url(r'^mypockets/None$', mypocket_, name='mypocket_'),

    url(r'^catchsenior$', catchsenior, name='catchsenior'),
    url(r'^doppelganger$', doppelganger, name='doppelganger'),

    url(r'^recognize$', recognize, name='recognize'),

    url(r'^rank/freshman$', rank_freshman, name='rank_freshman'),
    url(r'^rank/senior$', rank_senior, name='rank_senior'),

    url(r'^seniors$', seniors, name='seniors'),
    url(r'^seniors/(?P<pk>[0-9]+)$', senior, name='senior'),
    url(r'^seniors/(?P<spk>[0-9]+)/catching/(?P<cpk>[0-9]+)$', catching, name='catching'),

    url(r'^training$', training, name='training'),
    #url(r'^training_result$', training_result, name='training_result'),

]
