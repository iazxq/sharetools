# -*- coding: utf-8 -*-
import pymongo
from app.common import config
class DB:
    def __init__(self):
        self.conn = config.conn
        self.database = self.conn.tools


if __name__=='__main__':
    d = DB()
    print(d.database)


