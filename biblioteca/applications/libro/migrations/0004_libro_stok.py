# Generated by Django 4.0.5 on 2022-06-25 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_alter_libro_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='stok',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
