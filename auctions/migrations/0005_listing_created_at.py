# Generated by Django 5.0.2 on 2024-02-23 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listing_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 23, 14, 53, 53, 88009)),
        ),
    ]