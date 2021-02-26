# Generated by Django 3.1.6 on 2021-02-26 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210226_1338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventstate',
            options={'verbose_name': 'State', 'verbose_name_plural': 'States   '},
        ),
        migrations.AddField(
            model_name='eventcity',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.eventstate'),
        ),
    ]
