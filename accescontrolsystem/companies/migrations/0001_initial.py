# Generated by Django 4.0.3 on 2022-04-21 07:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccesPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('geolocation', models.CharField(max_length=250)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('commercial_address', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Invalid URL', regex='[(http(s)?):\\/\\/(www\\.)?a-zA-Z0-9@:%._\\+~#=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%_\\+.~#?&//=]*)')])),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('ending_time', models.TimeField()),
                ('acces_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules_acces_point', to='companies.accespoint')),
            ],
        ),
    ]
