# Generated by Django 3.2.3 on 2021-05-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210528_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='fees',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]