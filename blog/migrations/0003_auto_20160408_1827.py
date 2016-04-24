# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160407_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2016, 4, 8, 10, 27, 34, 399864, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30, default=datetime.datetime(2016, 4, 8, 10, 27, 44, 923466, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='Post_text',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
