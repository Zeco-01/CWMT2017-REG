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
        default = {'name' : a['name'], 'phone' : a['phone'], 'sex':a['sex'], 'phone': a['phone'], 'mail': a['email'], 'invoice': a['invoice'],'tax_id': a['tax_id'], 'address': a['address'], 'user_id': a['id'], 'paper_id': a['paper_id'],'stay': a['stay'], 'type' : a['type']}
        user, if_success = User.objects.get_or_create(mail = a['email'], defaults = default)

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
            user.save()
            strr =  '姓名: ' + user.name + '    '+ user.sex +'<br />' + '注册码: '+ str(user.register_number)+'<br />'
            strr += '电话: '+user.phone + '<br />'
            strr += 'e-mail: '+ user.mail + '<br />'
            strr += '发票抬头: ' + user.invoice + '<br />'
            strr += '发票纳税人识别号: ' + user.tax_id + '<br />'
            strr += '发票邮寄地址: ' + user.address + '<br />'
            strr += '身份证号: '+ user.user_id + '<br />'
            strr += '论文ID: '+ user.paper_id + '<br />'
            strr += '住宿方式: '
            if user.stay == 'no':
                strr += '自行解决'
            if user.stay == 'single':
                strr += '单间（350元 /人＊天）' + '<br />'
                strr += '入住日期: '+ user.in_date + ' - '+ user.out_date + '<br />'
            if user.stay == 'multi':
                strr += '合住（两人每天390元）'
                strr += '入住日期: '+ user.in_date + ' - ' + user.out_date + '<br />'
        else:
            strr = "create user failed because identical object exists: register number is: "+str(user.register_number)
        return HttpResponse(strr)


processor = Processor()
    # Create your views here.
