# -*- coding: utf-8 -*-
__author__ = 'Administrator'
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render_to_response
from app.common import config
from app.common import func
from app.facade import factory
from app.common import gvar

def Index(request):
    tools = config.Tools
    tool = tools.get('jiemeng',{})
    return render_to_response('dream/index.html',locals())

def Detail(request,id):
    tools = config.Tools
    tool = tools.get('jiemeng',{})
    dreamFacade = factory.CreateDreamFacade()
    dream = dreamFacade.Load(id=id)
    words = gvar.seg.cut(dream['title'].encode('utf8'))
    relatedDreams = dreamFacade.Search(keywords=words,count=100)
    catDreams = dreamFacade.Search(cat=dream.get('cat',''))
    return render_to_response('dream/detail.html',locals())

def Search(request):
    keyword = func.get_str_param_from_get(request,'jiemeng')
    dreamFacade = factory.CreateDreamFacade()
    dreams = dreamFacade.Search(title=keyword)
    if dreams['total_count'] > 0:
        dream = dreams['list'][0]
        return HttpResponseRedirect('/jiemeng/detail/%s/'%dream['_id'])
    return render_to_response('dream/search.html',locals())



