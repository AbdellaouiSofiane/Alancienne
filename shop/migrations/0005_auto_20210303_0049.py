# Generated by Django 3.1.7 on 2021-03-02 23:49

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210302_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tva',
            field=models.DecimalField(choices=[(Decimal('0.055'), '5,5 %'), (Decimal('0.2'), '20 %')], decimal_places=3, max_digits=4, verbose_name='tva'),
        ),
    ]