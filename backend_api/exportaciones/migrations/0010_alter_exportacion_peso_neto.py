# Generated by Django 5.0.6 on 2024-09-13 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exportaciones', '0009_alter_exportacion_año'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exportacion',
            name='peso_neto',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
