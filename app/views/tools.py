# -*- coding: utf-8 -*-
__author__ = 'Administrator'
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render_to_response
from app.common import config
from app.common import func,validator
import datetime

def ifconfig(request):
    '''查询本机ip地址'''
    tools = config.Tools
    tool = tools.get('ifconfig',{})
    return render_to_response('ifconfig.html',locals())

def timer(request):
    '''查询本机ip地址'''
    tools = config.Tools
    tool = tools.get('timer',{})
    return render_to_response('timer.html',locals())

def timershow(request,timeLength):
    '''倒计时'''
    tools = config.Tools
    tool = tools.get('timer',{})
    delay = 0 #默认为300秒，5分钟
    try:
        timeLength = timeLength.lower()
        #纯数字
        if validator.is_numeric(timeLength):
            delay = int(timeLength)

        #带seconds
        if timeLength.lower().endswith('seconds'):
            delay = int(timeLength.replace('seconds',''))

        #带minutes
        if timeLength.lower().endswith('minutes'):
            delay = int(timeLength.replace('minutes','')) * 60

        #带hours
        if timeLength.lower().endswith('hours'):
            delay = int(timeLength.replace('hours','')) * 60 * 60

        #带days
        if timeLength.lower().endswith('days'):
            delay = int(timeLength.replace('days','')) * 60 * 60 * 24
    except:
        pass

    startTime = func.getTimestamp(datetime.datetime.now())
    endTime = func.getTimestamp(datetime.datetime.now()+datetime.timedelta(seconds=delay))
    return render_to_response('timer-show.html',locals())