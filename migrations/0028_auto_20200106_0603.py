# Generated by Django 3.0 on 2020-01-06 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0027_auto_20200106_0559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='usr',
            new_name='username',
        ),
    ]
