# Generated by Django 3.1.6 on 2021-02-26 14:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_auto_20210226_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 26, 14, 2, 43, 889654, tzinfo=utc)),
        ),
    ]
