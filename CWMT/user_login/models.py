# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    #user_id = models.CharField(max_length=50) #user id
    name = models.CharField(max_length = 30) # user name
    sex = models.CharField(max_length = 20, blank = True) # user gender
    phone = models.CharField(max_length = 60, blank = True) # user phone number
    mail = models.CharField(max_length=200, blank = True) # user mail addr
    invoice = models.CharField(max_length = 200, blank = True) # user invoice
    tax_id = models.CharField(max_length=200, blank = True) # tax id number
    address = models.CharField(max_length= 1000, blank = True) # tax sending address
    user_id = models.CharField(max_length=50, blank = True) # user id
    paper_id = models.CharField(max_length=50, blank = True) # paper id
    stay = models.CharField(max_length=20) # room style
    m_name = models.CharField(max_length = 200, null=True ) # if room mate has a name
    type = models.CharField(max_length= 200, blank = True) # user type
    enter_date = models.CharField(max_length=100, blank = True) # login date
    out_date = models.CharField(max_length=100, blank = True) # logout date
    register_number = models.CharField(max_length=20, blank = True, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']



