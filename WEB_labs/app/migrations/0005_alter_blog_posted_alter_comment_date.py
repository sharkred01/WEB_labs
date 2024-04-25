# Generated by Django 5.0.4 on 2024-04-24 20:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_blog_image_alter_blog_posted_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 4, 25, 1, 9, 38, 831299), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 4, 25, 1, 9, 38, 831299), verbose_name='Дата'),
        ),
    ]
