# Generated by Django 4.0.4 on 2022-08-03 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_authuser_user_type'),
        ('bookingapp', '0005_alter_booking_approver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.faculty'),
        ),
    ]
