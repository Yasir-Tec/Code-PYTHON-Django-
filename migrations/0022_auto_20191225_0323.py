# Generated by Django 3.0 on 2019-12-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0021_auto_20191224_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='qua',
            field=models.CharField(default=0, max_length=30),
        ),
    ]