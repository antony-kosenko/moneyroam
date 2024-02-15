from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from moneyroam.views import StartingPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", StartingPageView.as_view(), name="start_page"),
    path("", include("invoices.urls")),
    path("accounts/", include("accounts.urls")),
    path("preferences/", include("preferences.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
