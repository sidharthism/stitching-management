# Generated by Django 4.0.2 on 2022-02-19 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
    ]
