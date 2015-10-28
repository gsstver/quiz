# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTestResult',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('datetime', models.DateField(auto_created=True)),
                ('data', jsonfield.fields.JSONField()),
                ('test', models.ForeignKey(related_name='results', to='main.Test')),
                ('user', models.ForeignKey(related_name='results', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
