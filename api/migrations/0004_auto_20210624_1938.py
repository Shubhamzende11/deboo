# Generated by Django 3.2.3 on 2021-06-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_transaction_w_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffprofile',
            name='photo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
