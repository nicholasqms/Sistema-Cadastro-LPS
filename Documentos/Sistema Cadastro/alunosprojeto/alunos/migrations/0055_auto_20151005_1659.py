# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0054_auto_20151004_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orientador',
            name='contato',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Telefone para Contato', blank=True),
        ),
    ]
