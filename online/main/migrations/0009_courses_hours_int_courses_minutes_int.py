# Generated by Django 4.0.4 on 2022-06-12 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_courses_hours_courses_minutes'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='hours_int',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='courses',
            name='minutes_int',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
