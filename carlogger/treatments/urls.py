from django.conf.urls.defaults import patterns, url

from carlogger.treatments.views import TreatmentListView, TreatmentDetailView
from carlogger.treatments.views import TreatmentCreateView


urlpatterns = patterns('carlogger.treatments.views',
    url(r'^$', TreatmentListView.as_view(), name='list'),
    url(r'^create/$', TreatmentCreateView.as_view(), name='create'),
    url(r'^(?P<treatment_pk>\d+)$', TreatmentDetailView.as_view(), name='detail'),
)
