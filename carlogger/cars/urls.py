from django.conf.urls.defaults import patterns, url, include

from carlogger.cars.views import CarListView, CarDetailView


urlpatterns = patterns('carlogger.cars.views',
                       url(r'^$', CarListView.as_view(), name='list'),
                       url(r'^(?P<pk>\d+)/$', CarDetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>\d+)/treatments/', include('carlogger.treatments.urls', namespace='treatments')),
                       )
