from preferences.forms import PreferencesGeneral


def preferences_form(request):
    """ Contains forms for preferences setup. """
    current_user_config = request.user.config
    preferences_form = PreferencesGeneral(instance=current_user_config)
    return {"preferences_form": preferences_form}