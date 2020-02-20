# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-12 10:35
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', multiselectfield.db.fields.MultiSelectField(choices=[('action', 'action'), ('drama', 'drama'), ('comedy', 'comedy')], default='action', max_length=19)),
                ('country', models.CharField(choices=[('eg', 'egypt'), ('us', 'america'), ('fr', 'france')], default='eg', max_length=100)),
                ('watched', models.BooleanField(default=False)),
                ('link', models.CharField(max_length=100)),
                ('overview', models.TextField(max_length=100)),
                ('vote_count', models.IntegerField(null=True)),
                ('vote_average', models.FloatField(max_length=100, null=True)),
                ('release_date', models.DateField(max_length=100, null=True)),
                ('lang', models.CharField(max_length=100)),
                ('img', models.ImageField(default='default.jpg', upload_to='profile_pics')),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='Movie',
            field=models.ManyToManyField(to='movie.Movie'),
        ),
    ]