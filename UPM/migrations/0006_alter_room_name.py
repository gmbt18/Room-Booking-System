# Generated by Django 4.0.4 on 2022-07-11 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPM', '0005_rename_slugs_building_slug_rename_slugs_college_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=300, null=True, unique=True),
        ),
    ]
