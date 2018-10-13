# Generated by Django 2.1.1 on 2018-10-13 10:27

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('moviepanel', '0003_auto_20181013_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviecategory',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='moviecategory',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]