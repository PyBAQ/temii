# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Charla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('prerequisitos', models.TextField(null=True, blank=True)),
                ('estado', models.CharField(max_length=255, choices=[(b'posible', b'Temas Posibles'), (b'agendado', b'Temas agendados'), (b'finalizado', b'Temas finalizados')])),
                ('fecha_taller', models.DateField()),
                ('votos', models.PositiveIntegerField(default=0)),
                ('categorias', models.ManyToManyField(to='votos.Categoria')),
            ],
            options={
                'ordering': ['votos'],
            },
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('charla', models.ForeignKey(to='votos.Charla')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='voto',
            unique_together=set([('usuario', 'charla')]),
        ),
    ]
