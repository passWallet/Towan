# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(help_text=b'Bitcoin Address', unique=True, max_length=34, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
