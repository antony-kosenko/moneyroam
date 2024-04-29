from django import forms

from preferences.models import Config


class PreferencesGeneral(forms.ModelForm):
    """ Form to update Preference instance """
    class Meta:
        model = Config
        exclude = ("user",)