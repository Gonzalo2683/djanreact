# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_proyecto_actualizado'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]
