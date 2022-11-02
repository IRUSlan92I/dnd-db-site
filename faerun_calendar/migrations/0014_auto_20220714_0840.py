# Generated by Django 3.2.12 on 2022-07-14 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faerun_calendar', '0013_alter_calendardata_current_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='YearData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.SmallIntegerField(verbose_name='Year')),
            ],
        ),
        migrations.RemoveField(
            model_name='calendardata',
            name='current_month',
        ),
        migrations.RemoveField(
            model_name='calendardata',
            name='current_year',
        ),
        migrations.RemoveField(
            model_name='calendardata',
            name='leap_month',
        ),
        migrations.RemoveField(
            model_name='event',
            name='month',
        ),
        migrations.RemoveField(
            model_name='event',
            name='year',
        ),
        migrations.AddField(
            model_name='monthdata',
            name='is_leap_month',
            field=models.BooleanField(default=0, verbose_name='IsLeapMonth'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DayData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(unique=True, verbose_name='Number')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faerun_calendar.monthdata')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faerun_calendar.yeardata')),
            ],
        ),
        migrations.AlterField(
            model_name='calendardata',
            name='current_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faerun_calendar.daydata'),
        ),
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faerun_calendar.daydata'),
        ),
    ]
