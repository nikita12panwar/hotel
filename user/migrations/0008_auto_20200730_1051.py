# Generated by Django 2.2 on 2020-07-30 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200730_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(max_length=20),
        ),
    ]
