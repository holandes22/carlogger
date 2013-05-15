from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin, SelectRelatedMixin

from carlogger.core.views import ByUserMixin
from carlogger.cars.models import Car
from carlogger.cars.forms import CarForm


class CarListView(LoginRequiredMixin, ByUserMixin, ListView):

    model = Car


class CarDetailView(LoginRequiredMixin, SelectRelatedMixin, ByUserMixin, DetailView):

    model = Car
    select_related = ['user', 'car']


class CarCreateView(LoginRequiredMixin, CreateView):

    form_class = CarForm
    template_name = 'editor.html'

    def get_success_url(self):
        return reverse('cars:list')

    def form_valid(self, form):
        self.instance = form.instance
        form.instance.user = self.request.user
        return super(CarCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CarCreateView, self).get_context_data(**kwargs)
        context['submit_url'] = reverse('cars:create')
        return context
