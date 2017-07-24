# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcastserver', '0004_auto_20170724_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programinfo',
            name='category',
            field=models.CharField(choices=[('Government & Organizations', 'Government & Organizations'), ('Games & Hobbies', 'Games & Hobbies'), ('Religion & Spirituality', 'Religion & Spirituality'), ('Music', 'Music'), ('Business', 'Business'), ('News & Politics', 'News & Politics'), ('Sports & Recreation', 'Sports & Recreation'), ('Health', 'Health'), ('Technology', 'Technology'), ('TV & Film', 'TV & Film'), ('Arts', 'Arts'), ('Comedy', 'Comedy'), ('Society & Culture', 'Society & Culture'), ('Education', 'Education'), ('Kids & Family', 'Kids & Family'), ('Science & Medicine', 'Science & Medicine')], max_length=20),
        ),
    ]
