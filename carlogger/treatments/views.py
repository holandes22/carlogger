import logging
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from carlogger.treatments.models import Treatment
from carlogger.cars.models import Car


log = logging.getLogger(__name__)


class ByCarMixin(object):

    def get_queryset(self):
        return self.model.objects.filter(car=self.get_car_object())

    def get_car_object(self):
        return get_object_or_404(Car, pk=self.kwargs['pk'])


class TreatmentListView(ByCarMixin, ListView):

    model = Treatment


class TreatmentDetailView(DetailView):

    model = Treatment
