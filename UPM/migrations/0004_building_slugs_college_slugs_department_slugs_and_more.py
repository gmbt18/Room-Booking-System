# Generated by Django 4.0.4 on 2022-07-11 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPM', '0003_term_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='slugs',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='college',
            name='slugs',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='slugs',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='slugs',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='term',
            name='slugs',
            field=models.SlugField(null=True),
        ),
    ]
