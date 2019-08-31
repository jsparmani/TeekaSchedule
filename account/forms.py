from django import forms
from location import models as loc_models


class ParentUsernameForm(forms.Form):

    username = forms.IntegerField(required=True)


class ParentOTPForm(forms.Form):

    otp = forms.IntegerField(required=True)


class ParentDetailsForm(forms.Form):

    f_name = forms.CharField()
    m_name = forms.CharField()
    f_dob = forms.DateField()
    m_dob = forms.DateField()

    def __init__(self, *args, **kwargs):
        super(ParentDetailsForm, self).__init__(*args, **kwargs)

        LOCALITY_CHOICES = [
            (x, x) for x in [u['name'] for u in loc_models.Locality.objects.all().values('name')]]

        self.fields['address'] = forms.ChoiceField(choices=LOCALITY_CHOICES)
        self.fields['f_dob'].widget.attrs['id'] = 'date'
        self.fields['m_dob'].widget.attrs['id'] = 'date'
        self.fields['f_dob'].widget.attrs['class'] = 'datepicker'
        self.fields['m_dob'].widget.attrs['class'] = 'datepicker'
