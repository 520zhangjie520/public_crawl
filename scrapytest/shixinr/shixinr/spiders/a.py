# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import  ShixinrItem
import pymongo
class ASpider(scrapy.Spider):
    name = 'a'
    def start_requests(self):
        inames = '李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤'
        for s in inames:
            pn=0
            num=0
            while num < 2500:
                url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E8%A2%AB%E6%89%A7%E8%A1%8C%E4%BA%BA%E5%90%8D%E5%8D%95&cardNum=&iname='+s+'&areaName=&pn=' + str(pn) + '&rn=1000&ie=utf-8&oe=utf-8&format=json&t=1571967956637&cb=jQuery110206805110476335876_1571966199119&_=1571966199192'
                pn += 10
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
                    'Referer': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA&oq=%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598&rsv_pq=99774cf20038ef48&rsv_t=61cbMkY3TVgcuSJS6LSV0IfZNoDVH2Bpnlz8t9u86hz3xBQ5lGz7hEqT8dA&rqlang=cn&rsv_enter=1&rsv_dl=tb&inputT=5844&rsv_sug3=33&rsv_sug1=32&rsv_sug7=101&rsv_sug2=0&rsv_sug4=5844&rsv_sug=1'
                }
                yield scrapy.Request(url=url, headers=headers)
                num+=1
    def parse(self, response):
        res = response.text[46:-2]
        res = json.loads(res)
        data = res['data'][0]['result']
        cont = ShixinrItem()
        cont['data']=data
        yield cont