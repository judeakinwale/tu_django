# Generated by Django 3.1.6 on 2021-05-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='events_purchased',
            field=models.ManyToManyField(to='core.Event'),
        ),
    ]
