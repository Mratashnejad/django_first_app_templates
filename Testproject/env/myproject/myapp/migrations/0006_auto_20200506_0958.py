# Generated by Django 3.0.5 on 2020-05-06 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20200502_1328'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Creator',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='pubdate',
            new_name='pub_date',
        ),
        migrations.AlterField(
            model_name='article',
            name='headline',
            field=models.CharField(max_length=180),
        ),
    ]
