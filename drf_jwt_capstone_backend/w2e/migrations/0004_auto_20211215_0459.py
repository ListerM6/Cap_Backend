# Generated by Django 3.2.8 on 2021-12-15 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w2e', '0003_recipestosave_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipestosave',
            name='image',
        ),
        migrations.RemoveField(
            model_name='recipestosave',
            name='image_type',
        ),
        migrations.RemoveField(
            model_name='recipestosave',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='recipestosave',
            name='title',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='likes',
        ),
        migrations.AddField(
            model_name='recipestosave',
            name='label',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]