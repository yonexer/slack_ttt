# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slack',
            fields=[
                ('game_id', models.AutoField(serialize=False, auto_created=True, primary_key=True)),
                ('channel_id', models.CharField(default=b'', unique=True, max_length=80)),
                ('player1', models.CharField(default=b'', max_length=30)),
                ('player2', models.CharField(default=b'', max_length=30)),
                ('last_player', models.CharField(default=b'', max_length=30)),
                ('board', models.CharField(default=b'', max_length=300)),
            ],
            options={
                'db_table': 'game',
            },
        ),
    ]
