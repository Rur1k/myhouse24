# Generated by Django 3.2.4 on 2021-10-22 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0057_remove_flat_personal_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTransactionType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('number', models.CharField(max_length=128, unique=True)),
                ('date', models.DateField()),
                ('is_complete', models.BooleanField(default=1)),
                ('sum', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('description', models.TextField()),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.useradmin')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.apartmentowner')),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.settingtransactionpurpose')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.accounttransactiontype')),
            ],
        ),
    ]
