from django.contrib import admin
from accounts.models import CustomUser, Profile

# Models registration
admin.site.register(CustomUser)
admin.site.register(Profile)
