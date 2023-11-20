from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import Profile

DEFAULT_SETTINGS = {
    "currency": "$",
    "language": "English"
}

CURRENCY_CHOICE = (
    ("₴", "₴"),
    ("$", "$"),
    ("€", "€")
)

LANGUAGE_CHOICE = (
    ("En", _("English")),
    ("Ua", _("Ukrainian"))
)

class Config(models.Model):
    """ Represents user's preferences. """
    
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICE, default=DEFAULT_SETTINGS["currency"])
    language = models.CharField(max_length=56, choices=LANGUAGE_CHOICE, default=DEFAULT_SETTINGS["language"])
    

    class Meta:
        verbose_name = _("config")
        verbose_name_plural = _("configs")

    def __str__(self):
        return f"Config[{self.pk}] for Profile[{self.profile.pk}]"
