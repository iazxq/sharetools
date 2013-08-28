# -*- coding: utf-8 -*-
import pymongo
from bson.objectid import ObjectId
from db import DB
import random

class DreamRepository(DB):

    def __init__(self):
        DB.__init__(self)
        self.table = self.database.zgjm

    def Load(self,id):
        result = self.table.find_one({'_id':ObjectId(id)})
        return result

    def Save(self,data):
        self.table.save(data)
        return True

    def Remove(self,id):
        self.table.remove({'_id':ObjectId(id)})
        return True


    def AddHit(self,id):
        return self.table.update({'_id':ObjectId(id)},{'$inc':{'hit':1}})

    def Search(self,cat=None,title=None,keywords=None,sort='_id',desc=True,start=0,randomStart=False,count=10):
        condition = {}
        if cat:
            condition['cat'] = cat

        if title:
            condition['title'] = title
            #condition['title'] = {'$regex':title}

        if keywords:
            keywords = '|'.join(keywords)
            condition['title'] = {'$regex':keywords}

        cur = self.table.find(condition)
        if title and not cur.count():
            condition['title'] = {'$regex':title}
            cur = self.table.find(condition)

        #满足条件的总记录数
        totalCount = cur.count()
        #设定排序
        sortType = pymongo.ASCENDING
        if desc:
            sortType = pymongo.DESCENDING
        if randomStart:
            start = random.randint(0,totalCount)
        cur = cur.skip(start).limit(count).sort(sort, sortType)
        recordList =list()
        for item in cur:
            recordList.append(item)

        return {'list':recordList,'total_count':totalCount}

if __name__=='__main__':
    pass