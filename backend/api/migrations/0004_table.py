# Generated by Django 4.2.6 on 2023-10-21 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_advertisement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.SmallIntegerField()),
                ('outdoor', models.BooleanField()),
                ('status', models.CharField(choices=[('FREE', 'Free'), ('PENDING_OF_CONFIRMATION', 'Pending of confirmation'), ('BUSY', 'Busy')], default='FREE', max_length=255)),
                ('number', models.SmallIntegerField()),
                ('bar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bar')),
            ],
            options={
                'unique_together': {('number', 'bar')},
            },
        ),
    ]
