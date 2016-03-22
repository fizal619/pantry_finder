# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0002_pantry_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='pantry',
            options={'verbose_name_plural': 'Pantries'},
        ),
        migrations.AlterField(
            model_name='pantry',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='pantry',
            name='facebook',
            field=models.URLField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='pantry',
            name='instagram',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='pantry',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='pantry',
            name='twitter',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]