# Generated by Django 3.0.5 on 2020-05-05 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200506_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='name',
        ),
        migrations.AddField(
            model_name='main',
            name='About',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='Name',
            field=models.TextField(default='Newspaper'),
        ),
    ]
