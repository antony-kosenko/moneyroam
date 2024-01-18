from django.http import HttpResponseRedirect
from django.shortcuts import render

from preferences.forms import PreferencesGeneral
from preferences.models import Config


def preference_general_view(request):
    """ Handles general preferences configuration. """
    # retrieving config related to user sends request.
    try:
        config_to_update = Config.objects.get(user_id=request.user.id)
    except Config.DoesNotExist:
        config_to_update = None

    if request.method == "POST":
        form = PreferencesGeneral(request.POST, instance=config_to_update)
        if form.is_valid(): 
            form.save()
            HttpResponseRedirect(request.META.get('HTTP_REFERER', "/"))
    else:
        form = PreferencesGeneral(instance=config_to_update)
    return render(request, template_name="preferences/settings_menu_base.html", context={"base_config_form": form})
