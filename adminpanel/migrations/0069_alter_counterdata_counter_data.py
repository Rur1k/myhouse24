# Generated by Django 3.2.4 on 2021-10-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0068_alter_counterdata_counter_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counterdata',
            name='counter_data',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]