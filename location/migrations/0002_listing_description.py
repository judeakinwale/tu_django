# Generated by Django 3.1.2 on 2021-02-09 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
