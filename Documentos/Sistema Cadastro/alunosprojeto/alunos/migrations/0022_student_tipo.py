# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0021_studentuser_bolsa'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='tipo',
            field=models.CharField(default=b'Iniciacao Cientifica', max_length=30, choices=[(b'Ensino Medio', b'Ensino Medio'), (b'Iniciacao Cientifica', b'Iniciacao Cientifica'), (b'Mestrado', b'Mestrado'), (b'Doutorado', b'Doutorado')]),
        ),
    ]
