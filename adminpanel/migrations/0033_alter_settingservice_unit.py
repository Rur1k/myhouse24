# Generated by Django 3.2.4 on 2021-10-01 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0032_settingservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingservice',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.serviceunit'),
        ),
    ]
