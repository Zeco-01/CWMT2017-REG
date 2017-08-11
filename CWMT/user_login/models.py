# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    # id = models.(default=0) #user id
    name = models.CharField(max_length = 30,null=True,blank = True) # user name
    sex = models.CharField(max_length = 20,null=True,blank = True) # user gender
    phone = models.CharField(max_length = 60, default = '',blank = True) # user phone number
    mail = models.CharField(max_length=200,null=True,blank = True) # user mail addr
    invoice = models.CharField(max_length = 200,null=True,blank = True) # user invoice
    tax_id = models.CharField(max_length=200,null=True,blank = True) # tax id number
    address = models.CharField(max_length= 1000,null=True,blank = True) # tax sending address
    user_id = models.CharField(max_length=50,default='',blank = True) # user id
    paper_id = models.CharField(max_length=50,null=True,blank = True) # paper id
    stay = models.CharField(max_length=20,null=True,blank = True) # room style
    m_name = models.CharField(max_length = 200 ,null=True,blank = True) # if room mate has a name
    type = models.CharField(max_length= 200,null=True,blank = True) # user type
    in_date = models.CharField(max_length=100,null = True) # login date
    out_date = models.CharField(max_length=100,null=True) # logout date
    register_number = models.AutoField(unique=True, max_length=20,blank = True,primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']



