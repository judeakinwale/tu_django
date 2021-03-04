# Generated by Django 3.1.6 on 2021-03-04 14:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_auto_20210302_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='location.listingcategory'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='location.realtor'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]