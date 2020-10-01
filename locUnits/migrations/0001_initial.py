# Generated by Django 3.0.4 on 2020-09-25 19:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('last_15_days', models.BooleanField(default=False)),
                ('last_30_days', models.BooleanField(default=False)),
                ('last_45_days', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('locUnit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locUnits.LocUnit')),
            ],
        ),
    ]
