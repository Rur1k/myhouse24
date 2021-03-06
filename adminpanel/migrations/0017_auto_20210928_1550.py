# Generated by Django 3.2.4 on 2021-09-28 12:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0016_contactpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpagedopinfo',
            name='description_dop',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Краткий текст'),
        ),
        migrations.AlterField(
            model_name='aboutpageinfo',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Краткий текст'),
        ),
        migrations.AlterField(
            model_name='mainpagenearby',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание услуги'),
        ),
    ]
