# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-12 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20160511_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='images_path',
            field=models.CharField(choices=[('Amigo', 'Amigo'), ('Bici+Tequila', 'Bici Tequila'), ('Camino+M\xe1gico+Tequila', 'Camino M\xe1gico Tequila'), ('Cuatrimoto+hasta+la+pierda+bola', 'Cuatrimoto hasta la piedra bola'), ('Familia', 'Familia'), ('Nevado_de_Colima', 'Nevado de Colima'), ('Pareja+Adrenalina', 'Pareja Adrenalina'), ('Relajacion', 'Relajacion'), ('Tarz\xe1n', 'Tarz\xe1n'), ('Tirolesa', 'Tirolesa'), ('default', 'default')], default='default', max_length=100),
        ),
    ]