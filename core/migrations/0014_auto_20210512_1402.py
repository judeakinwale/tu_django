# Generated by Django 3.1.6 on 2021-05-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_profile_events_purchased'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]