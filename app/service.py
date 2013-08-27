# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import pymongo
def ClearKeyword():
    conn=pymongo.Connection('172.20.53.109')
    db=conn.tools
    collection = db.zgjm
    cur = collection.find()
    for item in cur:
        item['title'] = item['title'].replace(u'梦见','')
        collection.save(item)


if __name__=='__main__':
    ClearKeyword()