from django import forms


class AddChildForm(forms.Form):

    name = forms.CharField()
    dob = forms.DateField()
