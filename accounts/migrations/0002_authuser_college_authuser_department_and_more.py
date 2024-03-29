# Generated by Django 4.0.4 on 2022-07-01 06:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UPM', '0002_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UPM.college'),
        ),
        migrations.AddField(
            model_name='authuser',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UPM.department'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator(allowlist=['up.edu.ph'])]),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
    ]
