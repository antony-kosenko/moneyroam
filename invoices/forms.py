from tkinter import Widget
from django import forms
from django.utils.translation import gettext_lazy as _

from mptt.forms import TreeNodeChoiceField

from invoices.models import Transaction, Category


class NewInvoiceForm(forms.ModelForm):
    category = TreeNodeChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Transaction
        fields = ("operation", "title", "category", "value", "currency", "comment", "receipt")
        help_texts = {
            "operation": _("Money operation type (Incomes/Expenses).")
        }

class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ("title", "value", "category", "comment", "receipt")
        widgets = {
            "receipt"
        }