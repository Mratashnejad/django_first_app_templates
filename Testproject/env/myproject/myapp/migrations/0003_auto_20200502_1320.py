# Generated by Django 3.0.5 on 2020-05-02 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_article_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Headline',
            new_name='headline',
        ),
    ]
