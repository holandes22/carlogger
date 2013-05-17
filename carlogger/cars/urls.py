from django.conf.urls.defaults import patterns, url, include

from carlogger.cars.views import CarListView, CarDetailView
from carlogger.cars.views import CarCreateView, CarDeleteView, CarUpdateView


urlpatterns = patterns('carlogger.cars.views',
    url(r'^$', CarListView.as_view(), name='list'),
    url(r'^create/$', CarCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', CarDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/delete/$', CarDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/update/$', CarUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/treatments/', include('carlogger.treatments.urls',
                                             namespace='treatments')),
)
