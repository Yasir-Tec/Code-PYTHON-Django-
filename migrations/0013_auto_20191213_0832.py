# Generated by Django 3.0 on 2019-12-13 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_marks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marks',
            old_name='Gcount',
            new_name='count',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='Gname',
            new_name='name',
        ),
    ]
