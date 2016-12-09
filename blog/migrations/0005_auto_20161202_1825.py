# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161202_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorcelebre',
            name='nacimiento',
            field=models.DateTimeField(),
        ),
    ]
