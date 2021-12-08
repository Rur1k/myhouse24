# Generated by Django 3.2.4 on 2021-09-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0013_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Название услуги')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание услуги')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/website/services')),
            ],
        ),
    ]