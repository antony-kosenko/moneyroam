from django import forms

from accounts.models import CustomUser, Profile


class CustomUserForm(forms.ModelForm):
    """ Form to create CustomUser. """
    class Meta:
        model = CustomUser
        fields = ("email", "password")

class ProfileForm(forms.ModelForm):
    """ Form to create Profile. """
    username = forms.CharField(max_length=250)
    first_name = forms.CharField(max_length=250, required=False)
    last_name = forms.CharField(max_length=250, required=False)

    class Meta:
        model = Profile
        fields = ("username", "first_name", "last_name")