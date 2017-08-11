# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import User
import json


class Processor(object):
    def __init__(self):
        self.register_code = 0

    def user_login_view(self, request):
        return render(request,'reg.html')


    @csrf_exempt
    def record(self, request):

        strr = ''
        if request.method == 'POST':
            a = request.POST
            json_data = json.loads(request.body)
            a = json_data
        if request.method == 'GET':
            raise SyntaxError('GET request cannot use')

        default = {'name' : str(a['name']), 'phone' : str(a['phone']),'register_number':self.register_code, 'sex':a['sex'], 'phone': str(a['phone']), 'mail': a['email'], 'invoice': a['invoice'],'tax_id': str(a['tax_id']), 'address': a['address'], 'user_id': str(a['id']), 'paper_id': str(a['paper_id']),'stay': a['stay'], 'type' : a['type']}
        user, if_success = User.objects.get_or_create(mail = str(a['email']), defaults = default)

        if if_success == True:
            if a['stay'] == 'no':
                user.in_date = None
                user.out_date = None
                user.m_room = None
            if a['stay'] == 'single':
                user.in_date = str(a['in_date'])
                user.out_date = str(a['out_date'])
                user.m_room = None
            if a['stay'] == 'multi':
                user.in_date = str(a['in_date'])
                user.out_date = str(a['out_date'])
                user.m_room = str(a['m_name'])
            self.register_code = self.register_code + 1
            user.save()
            for x in user._meta.fields:
                strr = strr + str(x) + ':' + str(user._meta.fields[x])+'\n'
        else:
            strr = "create user failed because identical object exists: register number is: "+str(user.register_number)
        return HttpResponse(strr)


processor = Processor()
    # Create your views here.
