# Generated by Django 3.2.8 on 2021-12-03 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipesToSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=150)),
                ('image_type', models.CharField(max_length=10)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.IntegerField(default=0)),
                ('comment_box', models.TextField(max_length=500)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='w2e.recipestosave')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_id', models.IntegerField(default=0)),
                ('reply_box', models.TextField(max_length=500)),
                ('review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='w2e.reviews')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_id', models.IntegerField(default=0)),
                ('stars', models.IntegerField(default=0)),
                ('review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='w2e.reviews')),
            ],
        ),
    ]
