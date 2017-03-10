from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.views.static import serve

from .views import home, UserCreateView
from software.views import introduction

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', introduction, name='home'),

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),

    url(r'^software/', include('software.urls', namespace='software')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
