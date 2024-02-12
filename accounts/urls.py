from django.urls import path

from accounts.views import registration_view, login_view


app_name = "accounts"

urlpatterns = [
    path("login/", login_view, name="login_page"),
    path("registration/", registration_view, name="registration_page"),
]
