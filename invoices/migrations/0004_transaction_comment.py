# Generated by Django 4.2.4 on 2023-11-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_transaction_delete_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
