# Generated by Django 3.1.6 on 2021-06-29 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0019_auto_20210318_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='is_ticket_sent',
            field=models.BooleanField(default=False),
        ),
    ]