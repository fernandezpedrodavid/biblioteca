# Generated by Django 4.0.5 on 2022-06-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0004_autor_apellidos_autor_edad_autor_nacionalidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='seudonimo',
            field=models.CharField(blank=True, max_length=50, verbose_name='Seudonimo'),
        ),
    ]
