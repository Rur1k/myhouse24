# Generated by Django 3.2.4 on 2021-10-26 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0058_accounttransaction_accounttransactiontype'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounttransaction',
            name='account',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='accounttransaction',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.settingpaymentitem'),
        ),
        migrations.DeleteModel(
            name='AccountTransactionType',
        ),
    ]