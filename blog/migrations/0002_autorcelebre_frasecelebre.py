# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutorCelebre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
                ('nacimiento', models.DateTimeField(auto_now_add=True)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FraseCelebre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('frase', models.TextField()),
                ('creado', models.DateField(auto_now_add=True)),
                ('activo', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('autor_celebre', models.ForeignKey(to='blog.AutorCelebre')),
            ],
        ),
    ]
