# Generated by Django 2.2.5 on 2019-10-30 23:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='postID',
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]