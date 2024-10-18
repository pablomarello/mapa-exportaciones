# Generated by Django 5.0.6 on 2024-08-07 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
        ('rubros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='rubro_id',
        ),
        migrations.AddField(
            model_name='producto',
            name='rubro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rubros', to='rubros.rubro'),
        ),
    ]
