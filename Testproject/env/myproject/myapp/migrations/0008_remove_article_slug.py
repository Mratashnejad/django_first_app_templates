# Generated by Django 3.0.5 on 2020-05-09 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]
