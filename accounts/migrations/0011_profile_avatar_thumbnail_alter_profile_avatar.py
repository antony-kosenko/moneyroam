# Generated by Django 4.2.4 on 2024-02-27 12:51

import accounts.models
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar_thumbnail',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=95, scale=0.5, size=[50, 50], storage=accounts.models.OverwriteStorage()),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='accounts/default_profile_avatar.svg', force_format='WEBP', keep_meta=True, null=True, quality=95, scale=0.5, size=[500, 500], storage=accounts.models.OverwriteStorage(), upload_to=accounts.models.profile_avatar_path),
        ),
    ]