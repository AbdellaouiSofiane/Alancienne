# Generated by Django 3.1.7 on 2021-03-01 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210302_0027'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Cart',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='order',
            new_name='cart',
        ),
    ]