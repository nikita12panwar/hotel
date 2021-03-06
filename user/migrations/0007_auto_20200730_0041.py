# Generated by Django 2.2 on 2020-07-29 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_room_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'get_latest_by': ['id']},
        ),
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(default='', upload_to='media/image/'),
        ),
    ]
