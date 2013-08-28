# -*- coding: utf-8 -*-

from app.repository.dream import DreamRepository

class DreamFacade:
    def __init__(self):
        self.repository = DreamRepository()

    def Load(self,id):
        result= self.repository.Load(id=id)
        return result

    def AddHit(self,id):
        return self.repository.AddHit(id=id)

    def Save(self,data):
        result = self.repository.Save(data)
        return result

    def Search(self,cat=None,title=None,keywords=None,sort='_id',desc=True,start=0,randomStart=False,count=10):
        result = self.repository.Search(cat=cat,title=title,keywords=keywords,sort=sort,desc=desc,start=start,randomStart=randomStart,count=count)
        return result