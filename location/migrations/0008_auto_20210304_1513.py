# Generated by Django 3.1.6 on 2021-03-04 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0007_auto_20210304_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='location.listingcategory'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.realtor'),
        ),
    ]