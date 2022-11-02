# Generated by Django 3.2.12 on 2022-07-14 11:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faerun_calendar', '0016_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yeardata',
            name='year',
        ),
        migrations.AddField(
            model_name='yeardata',
            name='number',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.RegexValidator('^-?[1-9]\\d{0,3}$', 'Year must be not zero and between -9999 and 9999')], verbose_name='Number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='daydata',
            name='number',
            field=models.SmallIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='monthdata',
            name='number',
            field=models.SmallIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(18)], verbose_name='Number'),
        ),
    ]
