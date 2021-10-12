# Generated by Django 3.2.4 on 2021-10-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0043_alter_settingservice_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingPayCompany',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]