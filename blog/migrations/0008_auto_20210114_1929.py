# Generated by Django 3.1.5 on 2021-01-14 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_email',
            field=models.EmailField(default='', max_length=254, null=True),
        ),
    ]
