# Generated by Django 3.2.4 on 2021-11-03 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0072_invoice_sum'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceIsInvoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('currency', models.CharField(blank=True, max_length=128, null=True)),
                ('consumption', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12)),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.invoice')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.settingservice')),
                ('unit_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.serviceunit')),
            ],
        ),
    ]
