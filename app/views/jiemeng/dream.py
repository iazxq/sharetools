# -*- coding: utf-8 -*-
__author__ = 'Administrator'
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render_to_response
from app.common import config
from app.common import func
from app.facade import factory
from app.common import gvar
from django.views.decorators.cache import cache_page


DreamCatDict = {
    'renwu':u'人物',
    'shenti':u'身体',
    'qinggan':u'情感',
    'wupin':u'物品',
    'shenghuo':u'生活',
    'guishen':u'鬼神',
    'jianzhu':u'建筑',
    'dongwu':u'动物',
    'zhiwu':u'植物',
    'ziran':u'自然',
}



@cache_page(60 * 60 *24)
def Index(request):
    tools = config.Tools
    tool = tools.get('jiemeng',{})
    dreamFacade = factory.CreateDreamFacade()
    dreams = {}
    for k,v in DreamCatDict.items():
        dreams[k] = {'title':v,'list':dreamFacade.Search(cat=k,count=5000)['list']}
    keywordClassList = config.FontClassList
    return render_to_response('dream/index.html',locals())

def Detail(request,id):
    tools = config.Tools
    tool = tools.get('jiemeng',{})
    dreamFacade = factory.CreateDreamFacade()
    dream = dreamFacade.Load(id=id)
    words = gvar.seg.cut(dream['title'].encode('utf8'))
    relatedDreams = dreamFacade.Search(keywords=words,count=100)
    catDreams = dreamFacade.Search(cat=dream.get('cat',''))
    catName = DreamCatDict.get(dream.get('cat',''),'')
    dreamFacade.AddHit(id=id)
    keywordClassList = config.FontClassList
    return render_to_response('dream/detail.html',locals())

def Search(request):
    tools = config.Tools
    tool = tools.get('jiemeng',{})
    keyword = func.get_str_param_from_get(request,'jiemeng')
    dreamFacade = factory.CreateDreamFacade()
    if not keyword:
        dreams = dreamFacade.Search(randomStart=True)
    else:
        dreams = dreamFacade.Search(title=keyword)

    if dreams['total_count'] > 0:
        dream = dreams['list'][0]
        return HttpResponseRedirect('/jiemeng/detail/%s/'%dream['_id'])

    words = gvar.seg.cut(keyword.encode('utf8'))
    relatedDreams = dreamFacade.Search(keywords=words,count=100)
    keywordClassList = config.FontClassList
    return render_to_response('dream/search.html',locals())

@cache_page(60 * 60 *24)
def Cat(request,cat):
    tools = config.Tools
    tool = tools.get('jiemeng',{})
    catName = DreamCatDict.get(cat,'')
    dreamFacade = factory.CreateDreamFacade()
    dreams = dreamFacade.Search(cat=cat,count=3000)
    keywordClassList = config.FontClassList
    return render_to_response('dream/cat.html',locals())



