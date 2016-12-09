# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='actualizado',
            field=models.DateField(default=datetime.datetime(2016, 12, 6, 15, 17, 22, 344000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
