# Generated by Django 2.2.24 on 2021-11-30 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_info', models.CharField(max_length=120000000000000000)),
                ('project_image', models.ImageField(upload_to='')),
            ],
        ),
    ]