# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161202_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorcelebre',
            name='nacimiento',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
