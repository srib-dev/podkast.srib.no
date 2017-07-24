# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcastserver', '0002_person_programinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programinfo',
            name='category',
            field=models.CharField(choices=[('Comedy', 'Comedy'), ('Kids & Family', 'Kids & Family'), ('Society & Culture', 'Society & Culture'), ('Business', 'Business'), ('Government & Organizations', 'Government & Organizations'), ('Arts', 'Arts'), ('Religion & Spirituality', 'Religion & Spirituality'), ('Health', 'Health'), ('Education', 'Education'), ('TV & Film', 'TV & Film'), ('Science & Medicine', 'Science & Medicine'), ('Games & Hobbies', 'Games & Hobbies'), ('News & Politics', 'News & Politics'), ('Technology', 'Technology'), ('Music', 'Music'), ('Sports & Recreation', 'Sports & Recreation')], max_length=20),
        ),
    ]
