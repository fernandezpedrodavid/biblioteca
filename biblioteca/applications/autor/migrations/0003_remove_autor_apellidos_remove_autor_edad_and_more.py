# Generated by Django 4.0.5 on 2022-06-25 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0002_alter_autor_edad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='nacionalidad',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='nombre',
        ),
    ]
