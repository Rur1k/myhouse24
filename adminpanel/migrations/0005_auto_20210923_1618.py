# Generated by Django 3.2.4 on 2021-09-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0004_auto_20210923_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seoinfo',
            name='keyworld',
        ),
        migrations.AddField(
            model_name='seoinfo',
            name='keyword',
            field=models.TextField(blank=True, null=True, verbose_name='Keywords'),
        ),
        migrations.AlterField(
            model_name='mainpageinfo',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Кратский текст'),
        ),
        migrations.AlterField(
            model_name='mainpagenearby',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='mainpagenearby',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/website/nearby'),
        ),
        migrations.AlterField(
            model_name='seoinfo',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='seoinfo',
            name='page',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Page'),
        ),
    ]