# Generated by Django 4.0.4 on 2022-08-16 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0010_rename_equipments_booking_equipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='isEdited',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
