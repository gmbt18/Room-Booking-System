# Generated by Django 4.0.4 on 2022-07-10 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPM', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='room',
            field=models.ManyToManyField(related_name='room_term', to='UPM.room'),
        ),
    ]
