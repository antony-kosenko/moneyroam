from django.contrib import admin

from invoices.models import Transaction, Category


admin.site.register(Transaction)
admin.site.register(Category)