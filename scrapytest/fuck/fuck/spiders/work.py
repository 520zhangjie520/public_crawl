# -*- coding: utf-8 -*-
import scrapy,json
from ..items import FuckItem
import json

class WorkSpider(scrapy.Spider):
    name = 'fuck'
    def start_requests(self):
        num=835

        for i in range(540,840):
            num +=1
            url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId='+str(num)+'&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&_v=0.57405721&x-zp-page-request-id=29f7739cef794f5799416e74456d6385-1572351271487-147745&x-zp-client-id=32014adb-4550-4a21-bb99-e934903664ef'
            yield scrapy.Request(url=url)
    def parse(self, response):
        res=json.loads(response.text)
        data=res['data']['results']
        num=FuckItem()
        num['data']=data
        yield num

