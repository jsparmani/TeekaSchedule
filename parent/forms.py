from django import forms
from . import models
from datetime import datetime


class AddChildForm(forms.Form):

    name = forms.CharField()
    dob = forms.DateField()


class EditVaccineForm(forms.Form):

    def __init__(self, user, *args, **kwargs):
        super(EditVaccineForm, self).__init__(*args, **kwargs)
        vaccine_list = models.Vaccine.objects.all().filter(
            date__lte=datetime.now(), status__exact=False, child__parent__user__username__exact=user.username)
        for vaccine in vaccine_list:
            self.fields[vaccine.name] = forms.BooleanField(required=False)


class SetReminderForm(forms.Form):

    FREQUENCY_CHOICES = [(1, 'Daily'), (2, 'Alternate Day'), (7, 'Weekly')]

    reminder_days = forms.IntegerField()
    reminder_frequency = forms.ChoiceField(choices=FREQUENCY_CHOICES)
