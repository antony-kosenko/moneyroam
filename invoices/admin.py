from django.contrib import admin

from invoices.models import Transaction, Category
from mptt.admin import MPTTModelAdmin


admin.site.register(Transaction)
admin.site.register(Category, MPTTModelAdmin)
