from django.views.generic import ListView, DetailView

from braces.views import LoginRequiredMixin

from carlogger.core.views import ByUserMixin
from carlogger.cars.models import Car


class CarListView(LoginRequiredMixin, ByUserMixin, ListView):

    model = Car


class CarDetailView(LoginRequiredMixin, ByUserMixin, DetailView):

    model = Car
