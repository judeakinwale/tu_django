# Generated by Django 3.1.6 on 2021-02-26 13:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0009_auto_20210226_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 26, 13, 55, 45, 927706, tzinfo=utc)),
        ),
    ]
