# Generated by Django 3.2.4 on 2021-10-19 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0050_flat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentowner',
            name='house',
        ),
    ]
