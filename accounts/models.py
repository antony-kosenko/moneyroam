import uuid

from django_resized import ResizedImageField

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.urls import reverse
from django.core.files.storage import get_storage_class
from django.utils.translation import gettext_lazy as _

from accounts.managers import CustomUserManager


class OverwriteStorage(get_storage_class()):
    """ Overwrites an existing file if file provided in request has a same name. """
    def _save(self, name, content):
        self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name, max_length=None):
        return name


def profile_avatar_path(instance, filename):
    # uploading avatar to dynamic PATH
    extension = filename.split(".")[-1]
    return f"accounts/{instance.username}/profile_image/{instance.username}_avatar.{extension}"

def profile_avatar_thumbnail_path(instance, filename):
    # uploading avatar to dynamic PATH
    extension = filename.split(".")[-1]
    return f"accounts/{instance.username}/profile_image/{instance.username}_thumbnail.{extension}"

class CustomUser(AbstractBaseUser, PermissionsMixin):

    """Custom User model extends a pre-defined django AbstractUser model"""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True, blank=True, null=True)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    
    def __str__(self):
        return self.email


class Profile(models.Model):
    
    """ Profile model. Contains user's extra data. """
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    avatar = ResizedImageField(
        force_format="WEBP",
        size=[500, 500],
        crop=["middle", "center"],
        upload_to=profile_avatar_path,
        blank=True,
        null=True,
        max_length=500,
        storage=OverwriteStorage()
        )
    avatar_thumbnail = ResizedImageField(
        force_format="WEBP",
        size=[100, 100],
        crop=["middle", "center"],
        upload_to=profile_avatar_thumbnail_path,
        blank=True,
        null=True,
        storage=OverwriteStorage()
        )
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"username": self.username})
