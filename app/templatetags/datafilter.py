# -*- coding: utf-8 -*-
from django.template import Library
import datetime
from app.facade import factory

register = Library()

def get_department_type_title(department_type_id):
    '''根据部门类型编号得到部门类型标题'''
    departmentFacade = factory.CreateDepartmentTypeFacade()
    departmentType=departmentFacade.Load(id=department_type_id)
    if departmentType:
        return departmentType['title']
    else:
        return ''
register.filter(get_department_type_title)

def get_department_title(department_id):
    '''根据单位编号获得单位名称'''
    departmentFacade = factory.CreateDepartmentFacade()
    departmentTitle = departmentFacade.GetName(department_id)
    return departmentTitle
register.filter(get_department_title)

def get_dict_title(id,type):
    '''得到字典标题'''
    dictFacade = factory.CreateDictFacade()
    dict = dictFacade.Load(type,id)
    result = ''
    if dict:
        result = dict.get('title','')
    return result
register.filter(get_dict_title)

def get_person(person_id,field):
    '''得到职工个人信息'''
    personFacade = factory.CreatePersonFacade()
    person = personFacade.Load(id=person_id)
    if field and person:
        return person.get(field,'')
    else:
        return person
register.filter(get_person)

def get_sms_unread_count():
    smsFacade = factory.CreateSmsFacade()
    count=smsFacade.GetCount(state='unread')
    return count
register.filter(get_sms_unread_count)


if __name__ == "__main__":
    pass