# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 22:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0005_remove_trip_pictures'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TripImages',
            new_name='TripImage',
        ),
    ]