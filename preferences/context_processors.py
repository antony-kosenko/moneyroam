from preferences.forms import PreferencesGeneral
from preferences.models import Config

def preferences_update_form(request):
    """ Contains forms for preferences setup. """
    config_to_update = Config.objects.filter(user=request.user).first()
    preferences_update_form = PreferencesGeneral(instance=config_to_update)
    return {"preferences_form": preferences_update_form}