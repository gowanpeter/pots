# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('somepots', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Widget',
        ),
        migrations.AlterField(
            model_name='documentation',
            name='documentation_name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='exhibitionlookup',
            name='exhibition_name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='heathlinelookup',
            name='heath_line_name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='makerlookup',
            name='maker_name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='materiallookup',
            name='material_name',
            field=models.CharField(max_length=16, blank=True),
        ),
        migrations.AlterField(
            model_name='methodlookup',
            name='method_name',
            field=models.CharField(max_length=12, blank=True),
        ),
    ]
