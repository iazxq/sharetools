# -*- coding: utf-8 -*-
import pymongo
from bson.objectid import ObjectId
from db import DB

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

    def Search(self,cat=None,title=None,keywords=None,sort='_id',desc=True,start=0,count=10):
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
        print('total:%s'%totalCount)
        #设定排序
        sortType = pymongo.ASCENDING
        if desc:
            sortType = pymongo.DESCENDING
        cur = cur.skip(start).limit(count).sort(sort, sortType)
        recordList =list()
        for item in cur:
            recordList.append(item)

        return {'list':recordList,'total_count':totalCount}

if __name__=='__main__':
    pass