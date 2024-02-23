from django.http import HttpResponseRedirect
from django.shortcuts import render

from preferences.forms import PreferencesGeneral
from preferences.models import Config


def preferences_view(request):
    """ View to manage base preferences. """
    # Note: forms for a GET request are passed in preferences' app context processor for global acces.
    if request.method == "POST":
        config_to_update = Config.objects.filter(user=request.user).first()
        preferences_form = PreferencesGeneral(request.POST, instance=config_to_update)
        if preferences_form.is_valid():
            preferences_form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', "/"))
    return render(request, "preferences/preferences_config.html")
