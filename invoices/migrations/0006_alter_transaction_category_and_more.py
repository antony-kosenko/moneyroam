# Generated by Django 4.2.4 on 2023-12-13 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0005_alter_transaction_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='invoices.category'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='operation',
            field=models.CharField(choices=[('incomes', 'incomes'), ('expenses', 'expenses')], max_length=8, verbose_name='operation'),
        ),
    ]