# Generated by Django 4.0.5 on 2022-11-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faerun_calendar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='', max_length=2500, verbose_name='Description'),
            preserve_default=False,
        ),
    ]
