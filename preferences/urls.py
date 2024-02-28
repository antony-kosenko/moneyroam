from django.urls import path
from django.contrib.auth.decorators import login_required

from preferences.views import preferences_view

app_name = "preferences"

urlpatterns = [
    path("", login_required(preferences_view), name="preferences_update")
]