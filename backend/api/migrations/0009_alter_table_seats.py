# Generated by Django 4.2.6 on 2023-12-20 17:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_advertisement_reduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='seats',
            field=models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(95)]),
        ),
    ]