import scrapy
from ..items import LiepItem
import re
class a(scrapy.Spider ):
    name='wor'
    def start_requests(self):
        name=['销售','运营','总经理','开发']
        for i in name :
            for j in range(100):
                url='https://www.liepin.com/zhaopin/?isAnalysis=&dqs=&pubTime=&salary=&subIndustry=&industryType=&compscale=&key='+str(i)+'&init=-1&searchType=1&headckid=952bb1273f74e7e5&compkind=&fromSearchBtn=2&sortFlag=15&ckid=952bb1273f74e7e5&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=fw3F47vuJXKzz2u6l56qUQ%7EfA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_prime&d_ckId=301b6be1c20275404bd0f15a1208f5c9&d_curPage=0&d_pageSize=40&d_headId=301b6be1c20275404bd0f15a1208f5c9&curPage='+str(j)
                yield scrapy.Request(url=url)
    def parse(self, response):
        work=response.xpath('//ul[@class="sojob-list"]/li/div/div[1]/h3/a/text()').getall()
        company = response.xpath('//ul[@class="sojob-list"]/li/div/div[2]/p[1]/a/text()').getall()
        address = response.xpath('//ul[@class="sojob-list"]/li/div/div[1]/p[1]/@title').getall()
        # address=re.findall(r'<a href="https://www.liepin.com/cd/zhaopin/" data-selector="data-url" class="area"></a>')
        salary = response.xpath('//ul[@class="sojob-list"]/li/div/div[1]/p[1]/span[1]/text()').getall()
        time = response.xpath('//ul[@class="sojob-list"]/li/div/div[1]/p[2]/time/@title').getall()
        data=LiepItem()
        print(len(work),len(company),len(address),len(salary),len(time)    )
        li=[]
        for i in range(len(work)):
            li.append([work[i],company[i],address[i],salary[i],time[i]])
        data["wa"]=li
        yield data

