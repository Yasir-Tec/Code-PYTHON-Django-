# Generated by Django 3.0 on 2019-12-29 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0025_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='usr',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
