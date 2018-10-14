# Generated by Django 2.1.1 on 2018-10-14 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviepanel', '0005_auto_20181014_1452'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moviegenre',
            options={'verbose_name': 'Movie Genre', 'verbose_name_plural': 'Movie Genres'},
        ),
        migrations.AlterField(
            model_name='moviegenre',
            name='moviepanel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moviegenres', related_query_name='moviegenre', to='moviepanel.MoviePanel'),
        ),
        migrations.AlterField(
            model_name='moviegenre',
            name='name',
            field=models.CharField(max_length=112, null=True, verbose_name='Movie Genre'),
        ),
    ]
