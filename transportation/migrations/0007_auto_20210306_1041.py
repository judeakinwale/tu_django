# Generated by Django 3.1.6 on 2021-03-06 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0006_auto_20210306_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operator',
            old_name='join_date',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='transportation',
            old_name='list_date',
            new_name='timestamp',
        ),
    ]