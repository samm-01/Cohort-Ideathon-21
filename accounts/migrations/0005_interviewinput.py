# Generated by Django 2.2.24 on 2021-11-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211130_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_info', models.CharField(max_length=120000000000000000)),
                ('interview_image', models.ImageField(upload_to='')),
            ],
        ),
    ]