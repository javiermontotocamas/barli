# Generated by Django 4.2.6 on 2023-12-01 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_bar_email_remove_userprofile_email'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='advertisement',
            unique_together={('bar', 'product_name')},
        ),
    ]