# Generated by Django 2.1.1 on 2018-11-08 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviepanel', '0023_movie_is_trailer_scraped'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='is_trailer_scraped',
        ),
    ]
