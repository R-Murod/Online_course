# Generated by Django 4.0.4 on 2022-06-22 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_alter_comment_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('logo', models.ImageField(blank=True, default='', upload_to='upload')),
                ('description', models.CharField(max_length=300)),
                ('date', models.DateTimeField()),
                ('comment_id', models.IntegerField(default=0)),
                ('email', models.CharField(blank=True, default='', max_length=300)),
                ('subject', models.CharField(blank=True, default='', max_length=300)),
            ],
        ),
    ]