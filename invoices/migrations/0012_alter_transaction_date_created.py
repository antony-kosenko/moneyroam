# Generated by Django 4.2.4 on 2024-03-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0011_alter_transaction_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]