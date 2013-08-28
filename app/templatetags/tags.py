# -*- coding: utf-8 -*-
from django import template
from app.common import config
register = template.Library()

@register.inclusion_tag('shared/tools_list.html', takes_context=True)
def tools_list(context):
    request = context['request']
    tools = config.Tools
    colorClassList = config.ColorClassList
    return locals()


