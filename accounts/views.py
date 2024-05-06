from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.db import transaction
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages

from accounts.forms import CustomUserCreationForm, ProfileCreationForm, UserLoginForm, ProfileUpdateForm
from preferences.models import Config


def registration_view(request):
    """ View to create new user. """

    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileCreationForm(request.POST)
        if all([user_form.is_valid(), profile_form.is_valid()]):
            with transaction.atomic():
                # creating new user
                new_user = user_form.save()
                
                # creating new profile
                new_profile = profile_form.save(commit=False)
                new_profile.user = new_user
                new_profile.save()

                # creating config instance
                Config.objects.create(user=new_user)

            messages.success(request, message="Registration succeed. You can use your credentials now to log in.")
            return redirect(reverse("accounts:login"))
        else:
            messages.error(request, message="Please, enter a valid data.")
            return render(
                request, "accounts/registration_page.html",
                context={"user_form": user_form, "profile_form": profile_form}
                )
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileCreationForm()
        context = {"user_form": user_form, "profile_form": profile_form}
        return render(request, "accounts/registration_page.html", context=context)
    
def login_view(request):
    """ Login view for existing user. """

    if request.method == "POST":
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            email = user_form.cleaned_data["email"]
            password = user_form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("invoices:dashboard")
            else:
                messages.error(request, "User with given credentials not exist. Please try again.")
                return render(request, "accounts/login_page.html", context={"user_form": user_form})
        else:
            return render(request, "accounts/login_page.html", context={"user_form": user_form})

    else:
        user_form = UserLoginForm()
        return render(request, "accounts/login_page.html", context={"user_form": user_form})


def logout_view(request):
    """ Performs logout of logged in user. """
    logout(request)
    return redirect(reverse("accounts:login"))


def profile_update_view(request):
    """ Updates current Profile instance."""
    if request.method == "POST":
        current_profile = request.user.profile
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=current_profile)
        if profile_form.is_valid():
            instance = profile_form.save(commit=False)
            instance.avatar_thumbnail = profile_form.cleaned_data.get("avatar")
            instance.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', "/"))
        else:
            profile_form = ProfileUpdateForm()
            return render(request, "accounts/profile_settings.html", {'profile_form': profile_form})
    