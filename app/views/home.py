# -*- coding: utf-8 -*-
__author__ = 'Administrator'
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render_to_response
from app.common import config
def HtmlIndex(request,name):
    '''用于输出纯html的页面'''
    tools = config.Tools
    tool = tools.get(name,{})
    colorClassList = config.ColorClassList
    template = '%s.html'%name
    return render_to_response(template,locals())

def Index(request,):
    tools = config.Tools
    colorClassList = config.ColorClassList
    return render_to_response('index.html',locals())

def Sitemap(request):
    tools = config.Tools
    colorClassList = config.ColorClassList
    return render_to_response('sitemap.html',locals())



