from django.conf.urls import patterns, include, url
from django.contrib import admin
from carlogger.views import HomePageView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^cars/', include('carlogger.cars.urls', namespace='cars')),
    url(r'^admin/', include(admin.site.urls)),
)
