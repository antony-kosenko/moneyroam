from django.urls import path
from invoices.views import DashboardView, TransactionsListView, create_transaction_view

app_name = "invoices"

urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("transactions/", TransactionsListView.as_view(), name="transactions"),
    path("transactions/create", create_transaction_view, name="create_transaction"),
]
