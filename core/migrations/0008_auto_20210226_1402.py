# Generated by Django 3.1.6 on 2021-02-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210226_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=500),
        ),
    ]
