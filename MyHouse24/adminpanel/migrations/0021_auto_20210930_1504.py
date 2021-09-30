# Generated by Django 3.2.4 on 2021-09-30 12:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0020_alter_contactpage_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc_name',
            field=models.CharField(max_length=64, verbose_name='Название документа'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='static/img/website/document', validators=[django.core.validators.FileExtensionValidator(['pdf', 'jpg'])]),
        ),
    ]
