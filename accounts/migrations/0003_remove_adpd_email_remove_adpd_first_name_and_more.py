# Generated by Django 4.0.4 on 2022-07-13 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UPM', '0009_room_room_type'),
        ('accounts', '0002_authuser_college_authuser_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adpd',
            name='email',
        ),
        migrations.RemoveField(
            model_name='adpd',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='adpd',
            name='last_name',
        ),
        migrations.AddField(
            model_name='adpd',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UPM.college'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'faculty'), (2, 'staff'), (3, 'ocs'), (4, 'adpd'), (5, 'ao')], null=True),
        ),
        migrations.CreateModel(
            name='AO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UPM.college')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Administrative Officers',
            },
        ),
    ]
