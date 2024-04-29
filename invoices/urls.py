from django.urls import path
from django.contrib.auth.decorators import login_required

from invoices.views import (
    DashboardView,
    TransactionUpdateView,
    TransactionsListView,
    create_transaction_view,
    TransactionDeleteView,
    )

app_name = "invoices"

urlpatterns = [
    path("dashboard/", login_required(DashboardView.as_view()), name="dashboard"),
    path("transactions/", login_required(TransactionsListView.as_view()), name="transactions"),
    path("transactions/create", login_required(create_transaction_view), name="create_transaction"),
    path("transactions/delete/<int:pk>", login_required(TransactionDeleteView.as_view()), name="delete_transaction"),
    path("transactions/edit/<int:pk>", login_required(TransactionUpdateView.as_view()), name="update_transaction"),
]
