from django import forms
from django.utils.translation import gettext_lazy as _

from mptt.forms import TreeNodeChoiceField

from invoices.models import Transaction, Category


class DateInput(forms.DateInput):
    input_type = 'date'


class NewInvoiceForm(forms.ModelForm):
    category = TreeNodeChoiceField(queryset=Category.objects.all())
    date_purchased = forms.DateField(widget=DateInput)

    class Meta:
        model = Transaction
        fields = (
            "operation",
            "title",
            "category",
            "value",
            "currency",
            "comment",
            "receipt",
            "date_purchased"
            )
        help_texts = {
            "operation": _("Money operation type (Incomes/Expenses).")
        }

class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = (
            "title",
            "value",
            "category",
            "comment",
            "receipt",
            "date_purchased"
            )