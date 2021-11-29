# Generated by Django 3.2.4 on 2021-11-19 13:34

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0075_auto_20211109_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Название статуса')),
            ],
        ),
        migrations.CreateModel(
            name='MasterRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('comment', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('flat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.flat')),
                ('master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.useradmin')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.apartmentowner')),
                ('status', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.statusrequest')),
                ('type_master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.userrole')),
            ],
        ),
    ]
