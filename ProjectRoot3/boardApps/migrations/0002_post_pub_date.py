# Generated by Django 4.0 on 2022-01-06 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardApps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 16, 34, 59, 878118), verbose_name='date published'),
        ),
    ]