# Generated by Django 4.0.3 on 2022-04-25 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists'}, max_length=254, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_company', to='companies.company')),
            ],
        ),
    ]