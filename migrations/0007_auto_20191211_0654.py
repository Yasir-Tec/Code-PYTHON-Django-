# Generated by Django 3.0 on 2019-12-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20191211_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='dept1',
            field=models.CharField(choices=[('cse', 'CSE'), ('mech', 'MECH'), ('civil', 'CIVIL'), ('auto', 'AUTO')], max_length=40, null=True),
        ),
    ]
