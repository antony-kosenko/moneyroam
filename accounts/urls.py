from django.urls import path
from django.contrib.auth.decorators import login_required

from accounts.views import registration_view, login_view, logout_view, profile_update_view


app_name = "accounts"

urlpatterns = [
    path("registration/", registration_view, name="registration"),
    path("login/", login_view, name="login"),
    path("logout/", login_required(logout_view), name="logout"),
    path("", login_required(profile_update_view), name="profile_update")
]
