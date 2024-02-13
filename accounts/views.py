from django.shortcuts import render

from accounts.forms import CustomUserForm, ProfileForm

# Create your views here.


def login_view(request):
    """ Login view for existing user. """
    return render(request, "accounts/login_page.html")

def registration_view(request):
    """ View to create new user. """

    if request.method == "POST":
        user_form = CustomUserForm(request.POST)
        profile_form = ProfileForm(request.POST)

    
    else:
        user_form = CustomUserForm()
        profile_form = ProfileForm()
        return render(request, "accounts/registration_page.html", context={"user_form": user_form, "profile_form": profile_form})
