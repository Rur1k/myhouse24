# Generated by Django 3.2.4 on 2021-10-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0052_account_statusaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='saldo',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
