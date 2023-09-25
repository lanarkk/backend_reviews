# Generated by Django 3.2 on 2023-09-24 20:12

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20230922_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveBigIntegerField(db_index=True, validators=[reviews.validators.validate_year], verbose_name='Год выпуска'),
        ),
    ]
