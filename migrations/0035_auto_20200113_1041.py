# Generated by Django 3.0 on 2020-01-13 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0034_auto_20200111_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='guide',
            name='fname',
            field=models.CharField(blank='NOT ALLOTED', default=True, max_length=40),
        ),
    ]