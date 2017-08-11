# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def user_login_view(request):
	print "user_login_view"
	return render(request,'reg.html')

@csrf_exempt
def record(request):
    a = request.POST
    print a
    return HttpResponse("1234567")


# Create your views here.
