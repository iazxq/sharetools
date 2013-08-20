# -*- coding: utf-8 -*-
__author__ = 'Administrator'
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render_to_response
from app.common import config
from app.common import func

def ifconfig(request):
    tools = config.Tools
    tool = tools.get('ifconfig',{})
    return render_to_response('ifconfig.html',locals())