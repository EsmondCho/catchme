from django.conf.urls import include, url
from django.contrib import admin

from .views import home
urlpatterns = [
    # Examples:
    # url(r'^$', 'catchme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home, name='home'),
    url(r'^software/', include('software.urls', namespace='software')),

]
