# Generated by Django 2.2.24 on 2021-12-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20211201_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinput',
            name='project_image',
            field=models.ImageField(blank=True, null=True, upload_to='Astra 2/media/images'),
        ),
    ]