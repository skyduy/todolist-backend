# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('context', models.TextField()),
                ('priority', models.IntegerField(default=0)),
                ('expired', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
