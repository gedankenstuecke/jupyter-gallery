# Generated by Django 2.0.5 on 2018-06-01 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180531_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharednotebook',
            name='data_sources',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='sharednotebook',
            name='created_at',
            field=models.DateTimeField(default='2018-05-25 20:05:21+00:00'),
        ),
        migrations.AlterField(
            model_name='sharednotebook',
            name='updated_at',
            field=models.DateTimeField(default='2018-05-25 20:05:21+00:00'),
        ),
    ]
