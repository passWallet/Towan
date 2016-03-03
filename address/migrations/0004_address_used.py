# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20151101_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
