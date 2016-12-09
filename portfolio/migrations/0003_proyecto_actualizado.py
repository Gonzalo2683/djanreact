# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_categoria_actualizado'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='actualizado',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 15, 22, 25, 47000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
