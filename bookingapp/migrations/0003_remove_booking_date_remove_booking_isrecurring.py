# Generated by Django 4.0.4 on 2022-07-06 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0002_booking_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='isRecurring',
        ),
    ]
