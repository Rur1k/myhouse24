# Generated by Django 3.2.4 on 2021-09-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0005_auto_20210923_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainpageslider',
            name='slide_1',
        ),
        migrations.RemoveField(
            model_name='mainpageslider',
            name='slide_2',
        ),
        migrations.RemoveField(
            model_name='mainpageslider',
            name='slide_3',
        ),
        migrations.AddField(
            model_name='mainpageslider',
            name='slide',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/website/slider'),
        ),
    ]
