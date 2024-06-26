# Generated by Django 4.2.4 on 2024-03-30 11:09

from django.db import migrations
import django_resized.forms
import invoices.models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0012_alter_transaction_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='receipt',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, max_length=500, null=True, quality=95, scale=0.5, size=[500, 500], upload_to=invoices.models.receipt_image_path),
        ),
    ]
