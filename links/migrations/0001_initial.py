# Generated by Django 4.0.5 on 2022-11-02 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField(verbose_name='Order')),
                ('url', models.CharField(max_length=250, verbose_name='URL')),
                ('text', models.CharField(max_length=250, verbose_name='Text')),
            ],
        ),
    ]
