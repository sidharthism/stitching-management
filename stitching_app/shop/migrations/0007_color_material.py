# Generated by Django 4.0.2 on 2022-02-19 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_item_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(default='', max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', max_length=30)),
                ('estimated_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
            ],
        ),
    ]