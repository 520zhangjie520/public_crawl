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
class WorkPipeline(object):
    def process_item(self, item, spider):
        cursor.executemany('insert into shop(ann_num,tmname,regname,reg_num) value("%s","%s","%s","%s");',item['data'])
        conn.commit()
