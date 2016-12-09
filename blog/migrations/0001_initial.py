# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cometario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=145)),
                ('contenido', models.TextField()),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
                ('publicado', models.DateTimeField(null=True, blank=True)),
                ('status', models.CharField(default=b'borrador', max_length=10, choices=[(b'borrador', b'Borrador'), (b'publicado', b'Publicado')])),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cometario',
            name='post',
            field=models.ForeignKey(related_name='comentarios', to='blog.Post'),
        ),
    ]
