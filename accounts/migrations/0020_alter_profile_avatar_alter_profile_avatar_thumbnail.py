# Generated by Django 4.2.4 on 2024-03-30 11:09

import accounts.models
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_profile_avatar_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='accounts/img/default_profile_avatar.svg', force_format='WEBP', keep_meta=True, max_length=500, null=True, quality=95, scale=0.5, size=[500, 500], storage=accounts.models.OverwriteStorage(), upload_to=accounts.models.profile_avatar_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar_thumbnail',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='accounts/img/default_profile_avatar.svg', force_format='WEBP', keep_meta=True, null=True, quality=95, scale=0.5, size=[100, 100], storage=accounts.models.OverwriteStorage(), upload_to=accounts.models.profile_avatar_thumbnail_path),
        ),
    ]