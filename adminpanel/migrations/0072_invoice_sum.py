# Generated by Django 3.2.4 on 2021-11-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0071_invoice_statusinvoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='sum',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
