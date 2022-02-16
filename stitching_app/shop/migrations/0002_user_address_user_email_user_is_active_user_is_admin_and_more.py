# Generated by Django 4.0.2 on 2022-02-16 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=255, unique=True, verbose_name='Email address'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_no',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
