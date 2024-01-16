from django.http import HttpResponseRedirect
from django.shortcuts import render

from preferences.forms import PreferencesGeneral
from preferences.models import Config


def preference_general_view(request):
    """ Handles general preferences configuration. """
    if request.method == "POST":
        form = PreferencesGeneral(instance=request.user)
        if form.is_valid:
            updated_config = Config(**form.cleaned_data)
            updated_config.save()
            HttpResponseRedirect(request.META.get('HTTP_REFERER', "/"))
    else:
        form = PreferencesGeneral(instance=request.user)
    return render(request, template_name="preferences/settings_menu_base.html", context={"base_config_form": form})
