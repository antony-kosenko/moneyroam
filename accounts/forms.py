from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    """ Form to create CustomUser. """
    required_css_class = "required"
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = CustomUser
        fields = ("email",)


class ProfileCreationForm(forms.ModelForm):
    """ Form to create Profile. """
    required_css_class = "required"
    username = forms.CharField(max_length=250)
    first_name = forms.CharField(max_length=250, required=False)
    last_name = forms.CharField(max_length=250, required=False)

    class Meta:
        model = Profile
        fields = ("username", "first_name", "last_name")

class UserLoginForm(forms.Form):
    """ Form to login User. """

    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
