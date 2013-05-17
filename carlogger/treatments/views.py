import logging

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from braces.views import LoginRequiredMixin

from carlogger.treatments.models import Treatment
from carlogger.treatments.forms import TreatmentForm
from carlogger.cars.models import Car


log = logging.getLogger(__name__)


class ByCarMixin(object):

    def get_queryset(self):
        return self.model.objects.filter(car=self.get_car_object())

    def get_car_object(self):
        return get_object_or_404(Car, pk=self.kwargs['pk'])


class TreatmentListView(LoginRequiredMixin, ByCarMixin, ListView):

    model = Treatment


class TreatmentDetailView(LoginRequiredMixin, DetailView):

    model = Treatment


class TreatmentCreateView(LoginRequiredMixin, ByCarMixin, CreateView):

    form_class = TreatmentForm
    template_name = 'editor.html'

    def get_success_url(self):
        return self.get_car_object().get_absolute_url()

    def form_valid(self, form):
        self.instance = form.instance
        form.instance.user = self.request.user
        form.instance.car = self.get_car_object()
        return super(TreatmentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TreatmentCreateView, self).get_context_data(**kwargs)
        context['submit_url'] = reverse('cars:treatments:create', kwargs=self.kwargs)
        context['success_url'] = self.get_success_url()
        return context

class TreatmentUpdateView(LoginRequiredMixin, UpdateView):

    form_class = TreatmentForm
    template_name = 'treatments/treatment_detail.html'

    def get_object(self):
        return Treatment.objects.get(pk=self.kwargs['treatment_pk'])

    def get_success_url(self):
        return self.get_object().car.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(TreatmentUpdateView, self).get_context_data(**kwargs)
        context['submit_url'] = reverse('cars:treatments:update', kwargs=self.kwargs)
        return context


class TreatmentDeleteView(LoginRequiredMixin, DeleteView):

    template_name = 'confirmation.html'

    def get_object(self):
        return Treatment.objects.get(pk=self.kwargs['treatment_pk'])

    def get_success_url(self):
        return reverse('cars:detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(TreatmentDeleteView, self).get_context_data(**kwargs)
        context['submit_url'] = reverse('cars:treatments:delete', kwargs=self.kwargs)
        context['success_url'] = self.get_success_url()
        return context
