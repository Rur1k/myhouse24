# Generated by Django 3.2.4 on 2021-09-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0012_auto_20210927_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='static/img/website/document')),
                ('doc_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Название документа')),
            ],
        ),
    ]
