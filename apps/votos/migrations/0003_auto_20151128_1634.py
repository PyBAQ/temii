# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votos', '0002_auto_20151128_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charla',
            name='estado',
            field=models.CharField(default=b'posible', max_length=255, choices=[(b'posible', b'Temas Posibles'), (b'agendado', b'Temas agendados'), (b'finalizado', b'Temas finalizados')]),
        ),
    ]
