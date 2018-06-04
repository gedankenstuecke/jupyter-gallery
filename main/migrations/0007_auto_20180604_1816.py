# Generated by Django 2.0.6 on 2018-06-04 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('open_humans', '0002_openhumansmember_oh_username'),
        ('main', '0006_auto_20180603_0453'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotebookLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default='2018-06-04 18:16:55+00:00')),
            ],
        ),
        migrations.AlterModelOptions(
            name='notebookcomment',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='sharednotebook',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='notebookcomment',
            name='created_at',
            field=models.DateTimeField(default='2018-06-04 18:16:55+00:00'),
        ),
        migrations.AlterField(
            model_name='sharednotebook',
            name='created_at',
            field=models.DateTimeField(default='2018-05-28 18:16:55+00:00'),
        ),
        migrations.AlterField(
            model_name='sharednotebook',
            name='updated_at',
            field=models.DateTimeField(default='2018-05-28 18:16:55+00:00'),
        ),
        migrations.AddField(
            model_name='notebooklike',
            name='notebook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.SharedNotebook'),
        ),
        migrations.AddField(
            model_name='notebooklike',
            name='oh_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='open_humans.OpenHumansMember'),
        ),
    ]
