# Generated by Django 3.1.6 on 2021-03-02 18:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_auto_20210302_1811'),
        ('payment', '0012_auto_20210226_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=200, null=True)),
                ('order_item_qty', models.IntegerField(blank=True, default=1, null=True)),
                ('amount_due', models.FloatField(blank=True, null=True)),
                ('is_ordered', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order_items', models.ManyToManyField(blank=True, null=True, to='core.Event')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('raw_request', models.TextField(blank=True, null=True)),
                ('event', models.CharField(blank=True, max_length=200, null=True)),
                ('data', models.CharField(blank=True, max_length=500, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.userorder')),
            ],
        ),
    ]
