from django.shortcuts import redirect, render
from django.db import transaction
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages

from accounts.forms import CustomUserCreationForm, ProfileCreationForm, UserLoginForm


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
                return render(request, "accounts/login_page.html", context={"user_form": user_form})
        else:
            return render(request, "accounts/login_page.html", context={"user_form": user_form})

    else:
        user_form = UserLoginForm()
        return render(request, "accounts/login_page.html", context={"user_form": user_form})

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
            # TODO messages for success/fail of registration
            messages.success(request, message="Registration succeed. You can use your credentials now to log in.")
            return redirect(reverse("accounts:login"))
        # TODO Create and style errors sections in case if form not valid
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
