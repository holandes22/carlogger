from django.views.generic import ListView, DetailView
from carlogger.core.views import ByUserMixin
from carlogger.cars.models import Car


class CarListView(ByUserMixin, ListView):

    model = Car


class CarDetailView(ByUserMixin, DetailView):

    model = Car
