# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def user_login_view(request):

    return render(request,'reg.html')

def record(request):
    a = request.POST
    return HttpResponse(a)


# Create your views here.
