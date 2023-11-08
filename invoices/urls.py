from django.urls import path
from invoices.views import CreateTransactionView, DashboardView

app_name = "invoices"

urlpatterns = [
    path("transactions/create", CreateTransactionView.as_view(), name="create_transaction"),
    path("dashboard", DashboardView.as_view(), name="dashboard")
]
