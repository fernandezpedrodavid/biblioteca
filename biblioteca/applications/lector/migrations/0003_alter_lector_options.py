# Generated by Django 4.0.5 on 2022-06-25 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0002_alter_prestamo_libro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lector',
            options={'verbose_name': 'Lector', 'verbose_name_plural': 'Lectores'},
        ),
    ]
