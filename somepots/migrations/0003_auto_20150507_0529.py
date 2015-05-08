# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('somepots', '0002_auto_20150502_1534'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logo_link_piece',
            options={'verbose_name_plural': 'logo pieces', 'verbose_name': 'logo link'},
        ),
    ]
