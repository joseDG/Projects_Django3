# Generated by Django 4.0.1 on 2022-01-26 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('shor_name', models.CharField(max_length=25, unique=True, verbose_name='Nombre Corto')),
            ],
            options={
                'verbose_name': 'Mi Departamento',
                'verbose_name_plural': 'Areas de la empresa',
                'ordering': ['-name'],
                'unique_together': {('name', 'shor_name')},
            },
        ),
    ]
