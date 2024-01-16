from django import forms

from preferences.models import Config


class PreferencesGeneral(forms.ModelForm):
    class Meta:
        model = Config
        exclude = ("user",)