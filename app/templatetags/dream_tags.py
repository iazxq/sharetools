# -*- coding: utf-8 -*-
from django import template
from app.common import config
from app.facade import factory
register = template.Library()

@register.inclusion_tag('dream/hot_keywords.html', takes_context=True)
def hot_keywords(context,count):
    dreamFacade = factory.CreateDreamFacade()
    dreams = dreamFacade.Search(sort='hit',count=count)
    keywordClassList = config.FontClassList
    return locals()


