from django.contrib import admin
from django.urls import include, path

from invoices.views import dashboard_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("invoices/", include("invoices.urls")),
]
