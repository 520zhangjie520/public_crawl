# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
conn = MySQLdb.connect(host="localhost",port=3306,user="root",password="123456",
                       db = "happy",charset="utf8"
                       )
cursor = conn.cursor()
class FuckPipeline(object):
    def process_item(self, item, spider):
        for i in item['data']:
            print(i['salary'])
            print(i['jobName'])
            print(i['workingExp']['name'])
            print(i['eduLevel']['name'])
            cursor.execute('insert into work(post,education,work,salary) value("%s","%s","%s","%s");',(i['jobName'],i['eduLevel']['name'],i['workingExp']['name'],i['salary']))
            conn.commit()


