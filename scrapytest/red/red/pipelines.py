# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
conn = MySQLdb.connect(host="localhost",port=3306,user="root",password="123456",
                       db = "happy",charset="utf8"
                       )
cursor=conn.cursor()
class RedPipeline(object):
    def process_item(self, item, spider):
        for i in item["data"]:
            print(i)
            cursor.execute('insert into  d(a,b,c) value("%s","%s","%s");' % (i[0],i[1],i[2]))
            conn.commit()
        return item
