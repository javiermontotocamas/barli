# Generated by Django 4.2.6 on 2023-12-20 22:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_table_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bar',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='table',
            name='seats',
            field=models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
    ]