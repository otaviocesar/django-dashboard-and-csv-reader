# Generated by Django 3.0.4 on 2020-10-01 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locUnits', '0002_auto_20200929_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='locunit',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
