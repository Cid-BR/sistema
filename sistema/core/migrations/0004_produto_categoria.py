# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-30 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180330_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Categoria'),
            preserve_default=False,
        ),
    ]
