# Generated by Django 3.2.4 on 2021-09-27 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0010_alter_mainpageinfo_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPageDopInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title_dop', models.CharField(blank=True, max_length=64, null=True, verbose_name='Заголовок')),
                ('description_dop', models.TextField(blank=True, null=True, verbose_name='Краткий текст')),
            ],
        ),
        migrations.CreateModel(
            name='AboutPageInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=64, null=True, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Краткий текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/website/about')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/img/website/about')),
                ('refers_to', models.CharField(blank=True, max_length=64, null=True, verbose_name='Пометка к чему относиться фото')),
            ],
        ),
    ]