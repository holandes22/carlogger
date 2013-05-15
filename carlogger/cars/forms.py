from django import forms

from carlogger.cars.models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ['user']
