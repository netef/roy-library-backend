# Generated by Django 5.0 on 2023-12-20 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 20, 15, 39, 15, 422325)),
        ),
        migrations.AlterField(
            model_name='book',
            name='img_url',
            field=models.CharField(max_length=255),
        ),
    ]