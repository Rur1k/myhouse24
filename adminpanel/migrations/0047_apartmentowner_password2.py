# Generated by Django 3.2.4 on 2021-10-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0046_apartmentowner'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentowner',
            name='password2',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]