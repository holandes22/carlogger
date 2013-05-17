from django import forms

from carlogger.treatments.models import Treatment


class TreatmentForm(forms.ModelForm):

    class Meta:
        model = Treatment
        exclude = ['user', 'car']
