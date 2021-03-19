# Generated by Django 3.1.5 on 2021-01-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_author_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contact_number',
            field=models.TextField(blank=True, help_text='If you have another way to comunicate.'),
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(default='www.exemplo.com', help_text='Paste here the link, witch you saw that news?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='Write your Post', null=True),
        ),
    ]
