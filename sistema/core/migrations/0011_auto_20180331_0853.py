# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-31 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_cliente_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(default='user.jpg', upload_to='media/'),
        ),
    ]
