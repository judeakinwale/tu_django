# Generated by Django 3.1.6 on 2021-03-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0010_auto_20210306_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingcategory',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='join_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
