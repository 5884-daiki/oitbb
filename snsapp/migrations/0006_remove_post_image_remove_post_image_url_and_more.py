# Generated by Django 4.2.2 on 2023-07-21 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0005_post_image_url_reply_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='image',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='image_url',
        ),
    ]
