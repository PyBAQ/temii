# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('votos', '0004_charla_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='charla',
            name='tallerista',
            field=models.ForeignKey(related_name='tallerista', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='charla',
            name='usuario',
            field=models.ForeignKey(related_name='propone_charla', to=settings.AUTH_USER_MODEL),
        ),
    ]
