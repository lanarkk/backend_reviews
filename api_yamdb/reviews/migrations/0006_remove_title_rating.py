# Generated by Django 3.2 on 2023-09-17 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_review_unique_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
    ]