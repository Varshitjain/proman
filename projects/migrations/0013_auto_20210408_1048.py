# Generated by Django 3.1.4 on 2021-04-08 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20210406_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assDate',
            field=models.DateField(default=datetime.datetime(2021, 4, 8, 10, 48, 26, 562443)),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 4, 8, 10, 48, 26, 562468)),
        ),
    ]
