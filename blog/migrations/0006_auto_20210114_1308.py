# Generated by Django 3.1.5 on 2021-01-14 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210114_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body_text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='number_of_comments',
        ),
        migrations.RemoveField(
            model_name='post',
            name='number_of_pingbacks',
        ),
        migrations.RemoveField(
            model_name='post',
            name='rating',
        ),
    ]
