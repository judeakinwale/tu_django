# Generated by Django 3.1.6 on 2021-05-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0013_auto_20210418_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
