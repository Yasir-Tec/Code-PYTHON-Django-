# users/models.py
import self as self
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
    Mobile_Number = models.CharField(max_length=10, default=True)
    department = (
        ('cse', 'CSE'),
        ('mech', 'MECH'),
        ('civil', 'CIVIL'),
        ('auto', 'AUTO')
    )
    select_dept = models.CharField(max_length=40, choices=department, default='CSE')

    # add additional fields in here

    def __str__(self):
        return self.username


''' THIS IS USER REGISTEARATION MODULE'''


class users(models.Model):
    title1 = models.CharField(max_length=50, default=True)

    fname1 = models.CharField(max_length=20, null=True)
    lname1 = models.CharField(max_length=20, null=True)

    departments = (
        ('cse', 'CSE'),
        ('mech', 'MECH'),
        ('civil', 'CIVIL'),
        ('auto', 'AUTO')
    )
    div = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    domains = (
        ('BLK', 'BLOCKCHAIN'),
        ('WEB', 'WEBSITE'),
        ('DB', 'DATABASE'),
        ('SC', 'NETWORKS-SECURITY'),
        ('AI', 'ARTIFICIAL-INTELLIGENTS'),
        ('DM', 'DATA-MINING')
    )
    aca = (
        ('18', '2018-19'),
        ('19', '2019-20'),
        ('20', '2020-21'),
        ('21', '2021-22'),
        ('22', '2022-23'),
        ('23', '2023-24'),
        ('24', '2024-25')

    )
    domainID = models.CharField(max_length=30, default=True)
    domains = models.CharField(max_length=100, choices=domains, default=True)
    aca = models.CharField(max_length=100, default=True, choices=aca)
    div1 = models.CharField(max_length=30, choices=div, default=5)

    dept1 = models.CharField(max_length=40, choices=departments, null=True)

    role1 = models.CharField(max_length=50, default='LEADER')

    email1 = models.EmailField(max_length=50, default=False)

    no1 = models.IntegerField(default=1234)

    email2 = models.EmailField(max_length=50, default=False)
    no2 = models.IntegerField(default=1234)

    teacher1 = models.CharField(max_length=30, default=True)
    res = models.CharField(max_length=30, default='yasir')
    qua = models.CharField(max_length=30, default=0)


class Teacher(models.Model):
    Tname = models.CharField(null=True, max_length=30)
    Ttopic = models.CharField(max_length=20, null=True)


class marks(models.Model):
    name = models.CharField(max_length=80, default='k')
    count = models.CharField(max_length=20, default='null')
    new = models.IntegerField(default=0)


class Store(models.Model):
    mod = models.CharField(max_length=20, default=True)
    smod = models.CharField(max_length=20, default=True)
    priority = models.CharField(max_length=20, default=True)
    status = models.CharField(max_length=20, default=True)
    teacher = models.CharField(max_length=30, default=True)
    title = models.CharField(max_length=30, default=True)


class addres(models.Model):
    type1 = models.CharField(max_length=20, default=True)
    nor = models.IntegerField(default=True)


class resources(models.Model):
    gname = models.CharField(max_length=100, default=True)
    restype = models.CharField(max_length=100, default=True)
    resqua = models.IntegerField(default=True)


file_choices = (
    ('synopsis', 'SYNOPSIS'),
    ('ppt', 'PPT'),
    ('report', 'REPORT')

)


class Document(models.Model):
    description = models.CharField(max_length=255, choices=file_choices, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, null=True)


class guide(models.Model):
    departments = (
        ('cse', 'CSE'),
        ('mech', 'MECH'),
        ('civil', 'CIVIL'),
        ('auto', 'AUTO')
    )
    degree = (
        ('Dr.', 'Dr.'),
        ('Prof.Dr.', 'Prof.Dr.'),
        ('Prof.', 'Prof.')

    )
    degree = models.CharField(max_length=40, choices=degree, blank=True)
    fname = models.CharField(max_length=40, default=True, blank='NOT ALLOTED')
    lname = models.CharField(max_length=40, default=True, blank=True)
    department = models.CharField(max_length=40, choices=departments, null=True)
    email = models.CharField(max_length=50, default=None, blank=True)
    mobile = models.CharField(max_length=50, default=None, blank=True)
    username = models.CharField(max_length=50, default=None, blank=True)
    password = models.CharField(max_length=50, default=None, blank=True)
