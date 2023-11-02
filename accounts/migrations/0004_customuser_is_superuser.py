# Generated by Django 4.2.4 on 2023-09-12 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_date_joined_customuser_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates whether the user has a superuser.', verbose_name='superuser'),
        ),
    ]