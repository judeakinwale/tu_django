# Generated by Django 3.1.6 on 2021-03-02 18:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210302_1811'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transportation', '0002_auto_20210209_2117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transportationcategory',
            options={'verbose_name': 'Category'},
        ),
        migrations.RenameField(
            model_name='transportationcategory',
            old_name='description',
            new_name='summary',
        ),
        migrations.RemoveField(
            model_name='transportationcategory',
            name='slug',
        ),
        migrations.AddField(
            model_name='transportation',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transportation',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.eventcity'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.eventstate'),
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
                ('description', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('is_trusted', models.BooleanField(default=False)),
                ('join_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
