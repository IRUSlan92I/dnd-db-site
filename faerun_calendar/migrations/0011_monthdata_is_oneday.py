# Generated by Django 3.2.12 on 2022-07-13 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faerun_calendar', '0010_alter_monthdata_folkname'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthdata',
            name='is_oneday',
            field=models.BooleanField(default=0, verbose_name='IsOneday'),
            preserve_default=False,
        ),
    ]
