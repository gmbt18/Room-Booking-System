# Generated by Django 4.0.4 on 2022-07-18 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_adpd_email_remove_adpd_first_name_and_more'),
        ('bookingapp', '0004_booking_dept_or_office_booking_equipments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='approver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.ao'),
        ),
    ]
