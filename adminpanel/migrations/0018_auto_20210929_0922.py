# Generated by Django 3.2.4 on 2021-09-29 06:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0017_auto_20210928_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='tariffspageinfo',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
