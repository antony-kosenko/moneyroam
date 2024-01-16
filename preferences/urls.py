from django.urls import path

from preferences.views import preference_general_view

app_name = "preferences"

urlpatterns = [
    path("", preference_general_view, name="preferences_general")
]