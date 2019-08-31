from django import forms


class ParentUsernameForm(forms.Form):

    username = forms.IntegerField(required=True)


class ParentOTPForm(forms.Form):

    otp = forms.IntegerField(required=True)


class ParentDetailsForm(forms.Form):

    f_name = forms.CharField()
    m_name = forms.CharField()
    f_dob = forms.DateField()
    m_dob = forms.DateField()
