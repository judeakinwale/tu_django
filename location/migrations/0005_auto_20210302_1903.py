# Generated by Django 3.1.6 on 2021-03-02 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_auto_20210302_1813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listingcategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='location.listingcategory', verbose_name='Category'),
        ),
    ]
