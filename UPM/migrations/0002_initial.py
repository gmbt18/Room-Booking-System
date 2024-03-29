# Generated by Django 4.0.4 on 2022-07-01 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('UPM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.faculty'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UPM.room'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='term',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UPM.term'),
        ),
        migrations.AddField(
            model_name='room',
            name='building',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UPM.building'),
        ),
        migrations.AddField(
            model_name='room',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UPM.college'),
        ),
        migrations.AddField(
            model_name='department',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UPM.college'),
        ),
        migrations.AddField(
            model_name='building',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UPM.college'),
        ),
    ]
