# Generated by Django 2.2.13 on 2021-04-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=111, null=True, unique=True),
        ),
    ]
