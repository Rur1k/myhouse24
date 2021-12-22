# Generated by Django 3.2.4 on 2021-12-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0084_invoice_counters_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatternPrintInvoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='static/adminpanel/doc/invoice')),
                ('is_default', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
