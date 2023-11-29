from django.db import models

from accounts.models import CustomUser

DEFAULT_SETTINGS = {
    "currency": "$",
    "language": "English"
}

CURRENCY_CHOICE = (
    ("UAH", "₴"),
    ("USD", "$"),
    ("EUR", "€")
)

LANGUAGE_CHOICE = (
    ("EN", "English"),
    ("UA", "Ukrainian")
)

class Config(models.Model):
    """ Represents user's preferences. """
    
    user = models.OneToOneField(CustomUser, related_name="config", on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICE, default=DEFAULT_SETTINGS["currency"])
    language = models.CharField(max_length=56, choices=LANGUAGE_CHOICE, default=DEFAULT_SETTINGS["language"])
    

    class Meta:
        verbose_name = ("config")
        verbose_name_plural = ("configs")

    def __str__(self):
        return f"Config[{self.pk}] for Profile[{self.user.pk}]"
