from django import forms
from . import models
from datetime import datetime


class AddChildForm(forms.Form):

    name = forms.CharField()
    dob = forms.DateField()


class EditVaccineForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(EditVaccineForm, self).__init__(*args, **kwargs)
        vaccine_list = models.Vaccine.objects.all().filter(
            date__lte=datetime.now(), status__exact=False)
        for vaccine in vaccine_list:
            self.fields[vaccine.name] = forms.BooleanField(required=False)
