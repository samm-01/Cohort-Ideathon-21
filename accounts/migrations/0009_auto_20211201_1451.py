# Generated by Django 2.2.24 on 2021-12-01 09:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_projectinput_project_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewinput',
            name='interview_date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2021, 12, 1, 9, 20, 43, 418870, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interviewinput',
            name='interview_time',
            field=models.TimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 1, 9, 21, 32, 941812, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
