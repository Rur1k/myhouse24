# Generated by Django 3.2.4 on 2021-12-16 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0082_message_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='saldo',
        ),
    ]
