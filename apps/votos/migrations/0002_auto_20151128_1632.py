# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charla',
            name='fecha_taller',
            field=models.DateField(null=True, blank=True),
        ),
    ]
