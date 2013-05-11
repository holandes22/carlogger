from django.conf.urls.defaults import patterns, url

from carlogger.treatments.views import TreatmentListView, TreatmentDetailView


urlpatterns = patterns('carlogger.treatments.views',
                       url(r'^$', TreatmentListView.as_view(), name='list'),
                       url(r'^(?P<treatment_pk>\d+)$', TreatmentDetailView.as_view(), name='detail'),
                       )
