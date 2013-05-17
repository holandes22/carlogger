from django.conf.urls.defaults import patterns, url

from carlogger.treatments.views import TreatmentListView, TreatmentDetailView
from carlogger.treatments.views import TreatmentCreateView, TreatmentUpdateView, TreatmentDeleteView


urlpatterns = patterns('carlogger.treatments.views',
    url(r'^$', TreatmentListView.as_view(), name='list'),
    url(r'^create/$', TreatmentCreateView.as_view(), name='create'),
    url(r'^(?P<treatment_pk>\d+)$', TreatmentDetailView.as_view(), name='detail'),
    url(r'^(?P<treatment_pk>\d+)/delete/$', TreatmentDeleteView.as_view(), name='delete'),
    url(r'^(?P<treatment_pk>\d+)/update/$', TreatmentUpdateView.as_view(), name='update'),
)
