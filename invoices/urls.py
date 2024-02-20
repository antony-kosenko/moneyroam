from django.urls import path
from django.contrib.auth.decorators import login_required

from invoices.views import DashboardView, TransactionsListView, create_transaction_view

app_name = "invoices"

urlpatterns = [
    path("dashboard/", login_required(DashboardView.as_view()), name="dashboard"),
    path("transactions/", login_required(TransactionsListView.as_view()), name="transactions"),
    path("transactions/create", login_required(create_transaction_view), name="create_transaction"),
]
