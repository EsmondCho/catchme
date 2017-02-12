from django.conf.urls import url

from .views import *

urlpatterns = [

    url(r'^$', introduction, name='introduction'),
    url(r'^mypocket$', mypocket, name='pocket'),
    url(r'^catchsenior$', catchsenior, name='catchsenior'),
    url(r'^recognize$', recognize, name='recognize'),
    url(r'^rank$', rank, name='rank'),

]