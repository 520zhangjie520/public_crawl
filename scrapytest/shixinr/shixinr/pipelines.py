# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import MySQLdb
# conn = MySQLdb.connect(host="localhost",port=3306,user="root",password="123456",
#                        db = "happy",charset="utf8"
#                        )
# cursor = conn.cursor()
import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017")
mydb=conn["shixinr"]
myset=mydb["fool"]
class ShixinrPipeline(object):
    def process_item(self, item, spider):
        print(item["data"] )
        for i in item["data"]:
            try:
                myset.insert([{"_id":i["caseCode"],"form":i}])
                # myset.insert([{"_id":i["caseCode"],'iname':i["iname"],'sexy':i["sexy"],'age':i["age"],'cardNum':i["cardNum"],'regDate':i["regDate"],'publishDate':i["publishDate"],'duty':i["duty"],'areaName':i["areaName"]}])
            except :
                pass
        # list1=[]
        # list1.append(item["data"] )
        # myset.insert(list1)
        # datas=myset.find()
        # for i in datas :
        #     print(i)

        # for i in item['data']:
            # print(i['duty'])
            # cursor.execute(
            #     'insert into shixin(casecode,iname,sexy,age,cardNum,regDate,publishDate,duty,areaName) value("%s","%s","%s","%s","%s","%s","%s","%s","%s");',(
            #     i['caseCode'], i['iname'], i['sexy'], i['age'], i['cardNum'], i['regDate'], i['publishDate'],i['duty'],i['areaName']))
            # conn.commit()
