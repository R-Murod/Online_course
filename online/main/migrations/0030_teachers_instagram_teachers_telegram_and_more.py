# Generated by Django 4.0.4 on 2022-06-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_emailaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='instagram',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='teachers',
            name='telegram',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='teachers',
            name='whatsapp',
            field=models.CharField(default='', max_length=300),
        ),
    ]