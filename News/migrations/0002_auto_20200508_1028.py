# Generated by Django 3.0.5 on 2020-05-08 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='cat_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='cat_name',
            field=models.CharField(default='newspaper', max_length=50),
        ),
        migrations.AddField(
            model_name='news',
            name='news_view',
            field=models.IntegerField(default=0),
        ),
    ]
