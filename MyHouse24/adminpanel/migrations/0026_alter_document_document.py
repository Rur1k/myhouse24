# Generated by Django 3.2.4 on 2021-09-30 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0025_auto_20210930_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='static/img/website/document', validators=[django.core.validators.FileExtensionValidator(allowed_extensions='jpg')]),
        ),
    ]
