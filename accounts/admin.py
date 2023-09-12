from django.contrib import admin
from accounts.models import CustomUser

# Models registration
admin.site.register(CustomUser)