# Generated by Django 2.2.24 on 2021-12-01 08:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20211201_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinput',
            name='project_time',
            field=models.TimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 1, 8, 43, 53, 285197, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
