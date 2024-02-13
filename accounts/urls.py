from django.urls import path

from accounts.views import registration_view, login_view


app_name = "accounts"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("registration/", registration_view, name="registration"),
]
