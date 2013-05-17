import logging

from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin, SelectRelatedMixin

from carlogger.core.views import ByUserMixin
from carlogger.cars.models import Car
from carlogger.cars.forms import CarForm


log = logging.getLogger(__name__)


class CarListView(LoginRequiredMixin, ByUserMixin, ListView):

    model = Car


class CarDetailView(LoginRequiredMixin, SelectRelatedMixin, ByUserMixin, DetailView):

    model = Car
    select_related = ['user', 'car']

    def get_context_data(self, **kwargs):
        context = super(CarDetailView, self).get_context_data(**kwargs)
        context['treatments'] = self.get_object().treatment_set.all()
        return context


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
        context['success_url'] = self.get_success_url()
        return context


class CarDeleteView(DeleteView):

    template_name = 'confirmation.html'

    def get_object(self):
        return Car.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('cars:list')

    def get_context_data(self, **kwargs):
        context = super(CarDeleteView, self).get_context_data(**kwargs)
        context['submit_url'] = reverse('cars:delete', kwargs=self.kwargs)
        context['success_url'] = self.get_success_url()
        return context


class CarUpdateView(UpdateView):

    form_class = CarForm
    template_name = 'editor.html'

    def get_object(self):
        return Car.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return self.get_object().get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(CarUpdateView, self).get_context_data(**kwargs)
        context['submit_url'] = reverse('cars:update', kwargs=self.kwargs)
        context['success_url'] = self.get_success_url()
        return context
