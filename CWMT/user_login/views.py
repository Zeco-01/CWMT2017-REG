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
        self.register_code = self.register_code + 1
        # for x in a:
        #     strr += x + ':' + a[x]+ "'\n'
        if request.method == 'POST':
            a = request.POST
            json_data = json.loads(request.body)
            a = json_data
        if request.method == 'GET':
            raise SyntaxError('GET request cannot use')

        default = {'sex':a['sex'], 'phone': a['phone'], 'mail': a['email'], 'invoice': a['invoice'],'tax_id': a['tax_id'], 'address': a['address'], 'user_id': a['id'], 'paper_id': a['paper_id'],'stay': a['stay'], 'type' : a['type']}
        user, if_success = User.objects.get_or_create(name = a['name'], phone = a['phone'], mail = a['email'], defaults = default)

        if if_success == True:
            if a['stay'] == 'no':
                user.enter_date = None
                user.out_date = None
                user.m_room = None
            if a['stay'] == 'single':
                user.enter_date = a['in_date']
                user.out_date = a['out_date']
                user.m_room = None
            if a['stay'] == 'multi':
                user.enter_date = a['in_date']
                user.out_date = a['out_date']
                user.m_room = a['m_name']
            user.register_number = str(self.register_code)
            user.save()
            for x in user._meta.fields:
                strr = strr + str(x) + ':' + str(user._meta.fields[x])+'\n'
        else:
            strr = "create user failed because identical object exists: register number is: "+str(user.register_number)
        return HttpResponse(strr)


processor = Processor()
    # Create your views here.
