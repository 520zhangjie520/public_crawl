# -*- coding: utf-8 -*-
import scrapy
import json
import time
from ..items import  WorkItem
class ExampleSpider(scrapy.Spider):
    name = 'example'
    def start_requests(self):
        post_url='http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearchDG.html'
        page=1
        num=1640
        for j in range(10):
            num+=1
            time.sleep(5)
            for i in range(10):
                page+=1
                time.sleep(2)
                formdata={
                    'page':str(page) ,
                    'rows': '1000',
                    'annNum': str(num) ,
                    'annType':'',
                    'tmType':'',
                    'coowner':'',
                    'recUserName':'',
                    'allowUserName':'',
                    'byAllowUserName':'',
                    'appId':'',
                    'appIdZhiquan':'',
                    'bfchangedAgengedName':'',
                    'changeLastName':'',
                    'transferUserName':'',
                    'acceptUserName':'',
                    'regName':'',
                    'tmName':'',
                    'intCls':'',
                    'fileType':'',
                    'totalYOrN': 'true',
                    'appDateBegin':'',
                    'appDateEnd':'',
                    'agentName':'',
                }
                yield scrapy.FormRequest(url=post_url, formdata=formdata)
    def parse(self, response):
        res = response.text
        res=eval(res)
        data=res['rows']
        li=[]
        for i in data:
            num=i['ann_num'],
            name=i['tmname'],
            rename=i['regname'],
            renum=i['reg_num']
            print(num,name)
            li.append([num, name, rename, renum])
            if li==[]:
                print(li)
            else:
                count=WorkItem()
                print(li)
                count['data']=li
                yield count


