# Generated by Django 3.1.6 on 2021-03-04 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0004_auto_20210302_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]