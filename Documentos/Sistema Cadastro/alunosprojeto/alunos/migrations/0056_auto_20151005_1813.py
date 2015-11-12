# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0055_auto_20151005_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rg_orgao_expeditor',
            field=models.CharField(default=b'\xc3\x93rg\xc3\xa3o Expeditor', max_length=20, verbose_name=b'\xc3\x93rg\xc3\xa3o Expeditor', validators=[b'string_validator']),
        ),
    ]
