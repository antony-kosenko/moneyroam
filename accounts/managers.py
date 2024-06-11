from django.contrib.auth.base_user import BaseUserManager
from django.db import transaction


from preferences.models import Config

class CustomUserManager(BaseUserManager):

    @transaction.atomic
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email and Username fields must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        # Creating superuser profile
        from accounts.models import Profile
        username_generated = email.split("@")[0]
        Profile.objects.create(user=user, username=username_generated)

        # creating config 
        Config.objects.create(user=user)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        new_user = self.create_user(email, password, **extra_fields)
        return new_user