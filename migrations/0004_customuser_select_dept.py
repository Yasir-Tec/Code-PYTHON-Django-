# Generated by Django 3.0 on 2019-12-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='select_dept',
            field=models.CharField(choices=[('cse', 'CSE'), ('mech', 'MECH'), ('civil', 'CIVIL'), ('auto', 'AUTO')], default='CSE', max_length=40),
        ),
    ]