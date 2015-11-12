# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0016_auto_20150914_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacheruser',
            name='username',
            field=models.CharField(unique=True, max_length=30, verbose_name=b'Username'),
        ),
    ]
