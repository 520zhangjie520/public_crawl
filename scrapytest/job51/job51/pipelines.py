# -*- coding: utf-8 -*-
# 把获取的data数据放入数据库
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
conn = MySQLdb.connect(host="localhost",port=3306,user="root",password="123456",
                       db = "happy",charset="utf8"
                       )
cursor = conn.cursor()

class Job51Pipeline(object):
    def process_item(self, item, spider):
        sql = "insert into job(post,company,salary) values(%s,%s,%s)"
        print(item['post'],item['company'],item['salary'])
        cursor.execute(sql, (item['post'],item['company'],item['salary']))
        conn.commit()
        return item

