# Generated by Django 4.2.4 on 2023-11-21 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='config',
            old_name='profile',
            new_name='user',
        ),
    ]
