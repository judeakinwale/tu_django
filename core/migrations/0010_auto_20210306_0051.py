# Generated by Django 3.1.6 on 2021-03-06 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_auto_20210302_1811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='featured',
            new_name='is_featured',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='active',
            new_name='is_published',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='location',
            new_name='street_address',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='price',
            new_name='ticket_price',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='sale_price',
            new_name='ticket_sale_price',
        ),
        migrations.AddField(
            model_name='event',
            name='ticket_quantity',
            field=models.IntegerField(default=50, verbose_name='Quantity'),
        ),
        migrations.AddField(
            model_name='event',
            name='ticket_quantity_sold',
            field=models.IntegerField(default=0, verbose_name='Quantity Sold'),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.eventcategory'),
        ),
        migrations.AlterField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
