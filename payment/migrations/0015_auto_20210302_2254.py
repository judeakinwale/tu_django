# Generated by Django 3.1.6 on 2021-03-02 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0014_auto_20210302_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='order_item_qty',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
