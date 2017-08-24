# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import User
import json
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail(my_user,s):
    ret = True
    my_sender = 'cwmt_2017@qq.com'  # 发件人邮箱账号
    my_pass = 'jgxufajzfoimbcbf'  # 发件人邮箱密码
    # my_user = 'cccaaag@126.com'  # 收件人邮箱账号，我这边发送给自己
    try:
        msg = MIMEText('您的注册信息如下：<br />'+s, 'html', 'utf-8')
        msg['From'] = formataddr(["CWMT2017会务组", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["CWMT2017参会注册人", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "请确认您的会议注册信息"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret
class Processor(object):
    def __init__(self):
        self.register_code = 0

    def user_login_view(self, request):
        return render(request,'reg.html')


    @csrf_exempt
    def record(self, request):
       

        strr = ''
        # return HttpResponse(strr)
        if request.method == 'POST':
            a = request.POST
            json_data = json.loads(request.body)
            a = json_data
        if request.method == 'GET':
            raise SyntaxError('GET request cannot use')
        default = {'name' : a['name'], 
        'sex':a['sex'], 
        'phone': a['phone'], 
        'mail': a['email'],
         'invoice': a['invoice'],
         'tax_id': a['tax_id'],  
         'user_id': a['id'], 
         'paper_id': a['paper_id'],
         'stay': a['stay'], 
         'type' : a['type'],
         'invoice_type':a['invoice_type']}
        user, if_success = User.objects.get_or_create(mail = a['email'], defaults = default)
        types = {
            'mg1':'普通会员-9月15日前缴费-1600元',
            'ms1':'学生会员-9月15日前缴费-1000元',
            'nms1':'非会员学生-9月15日前缴费-1100元',
            'nmg1':'非学生非会员-9月15日前缴费-1700元',
            'mg2':'普通会员-9月15日后缴费-1800元',
            'ms2':'学生会员-9月15日前缴费-1000元',
            'nms2':'非会员学生-9月15日后缴费-1300元',
            'nmg2':'非学生非会员-9月15日后缴费-1900元',
        }
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

            if a['invoice_type'] == 'sp':
                user.address = a['address']
                user.invoice_tel = a['invoice_tel']
                user.invoice_bank = a['invoice_bank']
                user.invoice_id = a['invoice_id']

            user.save()
            strr =  '姓名: ' + user.name + '<br />' 
            strr += '性别：'
            if user.sex == 'male':
                strr += '男'
            else:
                strr+='女'
            strr += '<br />注册码: ' + str(user.register_number)+'<br />'
            strr += '电话: '+user.phone + '<br />'
            strr += 'e-mail: '+ user.mail + '<br />'
            strr += '发票抬头: ' + user.invoice + '<br />'
            strr += '发票纳税人识别号: ' + user.tax_id + '<br />'
            strr += '发票类型：'+user.invoice_bank+'<br />'
            if a['invoice_type'] == 'sp':
                strr += '发票邮寄地址: ' + user.address + '<br />'
                strr += '电话：'+user.invoice_tel+'<br />'
                strr+= '开户银行：'+user.invoice_bank+'<br />'
                strr+= '账户：'+user.invoice_id+'<br />'
            strr += '身份证号: '+ user.user_id + '<br />'
            strr += '论文ID: '+ user.paper_id + '<br />'
            strr += '住宿方式: '
            if user.stay == 'no':
                strr += '自行解决'
            if user.stay == 'single':
                strr += '单间（350元 /人＊天）' + '<br />'
                strr += '入住日期: '+ user.in_date + ' - '+ user.out_date + '<br />'
            if user.stay == 'multi':
                strr += '合住（两人每天390元）'+ '<br />'
                if user.m_room=='yes':
                    strr+='有合住人姓名'+ '<br />'
                else:
                    strr+='无合住人姓名'+ '<br />'
                strr += '入住日期: '+ user.in_date + ' - ' + user.out_date + '<br />'
            strr +='注册类型：' +types[user.type]+'<br />'
            mail(user.mail,strr)
        else:
            strr = "使用相同手机号码的用户已经注册，请使用其他手机号码"
        return HttpResponse(strr)


processor = Processor()
    # Create your views here.
