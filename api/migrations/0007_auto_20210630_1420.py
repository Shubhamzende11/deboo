# Generated by Django 3.2.3 on 2021-06-30 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210629_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]