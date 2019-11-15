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
class LovePipeline(object):
    def process_item(self, item, spider):
            # for i in item['data']:
            #     print(i)
        # for i in item['data'] :
        #     print(i)
        cursor.executemany('insert into love(name,age,sex) value("%s","%s","%s");', item['data'] )
        # 需要先分类，在包装成一个二维列表
        conn.commit()


