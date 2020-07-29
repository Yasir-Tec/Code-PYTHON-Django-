# Generated by Django 3.0 on 2019-12-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0017_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='add',
        ),
        migrations.RemoveField(
            model_name='store',
            name='name',
        ),
        migrations.RemoveField(
            model_name='store',
            name='no',
        ),
        migrations.AddField(
            model_name='store',
            name='mod',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='store',
            name='priority',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='store',
            name='smod',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='store',
            name='status',
            field=models.CharField(default=True, max_length=20),
        ),
    ]