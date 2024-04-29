from accounts.forms import ProfileUpdateForm


def profile_update_form(request):
    """ Contains forms for preferences setup. """
    profile_form = ProfileUpdateForm()
    return {"profile_form": profile_form}