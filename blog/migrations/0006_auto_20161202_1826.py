# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161202_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frasecelebre',
            name='creado',
            field=models.DateField(),
        ),
    ]
