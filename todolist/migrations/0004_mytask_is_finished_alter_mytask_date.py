# Generated by Django 4.1 on 2022-09-28 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_mytask_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytask',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mytask',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 9, 28, 15, 24, 11, 486795)),
        ),
    ]
