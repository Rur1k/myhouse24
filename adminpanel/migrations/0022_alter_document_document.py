# Generated by Django 3.2.4 on 2021-09-30 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0021_auto_20210930_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='static/img/website/document'),
        ),
    ]
