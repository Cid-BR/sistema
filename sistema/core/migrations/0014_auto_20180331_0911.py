# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-31 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20180331_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(default='cliente_default.png', upload_to=''),
        ),
    ]