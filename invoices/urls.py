from django.urls import path
from invoices.views import CreateTransactionView, DashboardView, TransactionsListView

app_name = "invoices"

urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("transactions/", TransactionsListView.as_view(), name="transactions"),
    path("transactions/create", CreateTransactionView.as_view(), name="create_transaction"),
]
