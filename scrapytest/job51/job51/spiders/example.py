# -*- coding: utf-8 -*-
import scrapy
from ..items import Job51Item
import re
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

class ExampleSpider(scrapy.Spider):
    name = 'example'

    def start_requests(self):
        page_number = 1
        while 1:
            url='https://search.51job.com/list/000000,000000,0000,00,9,99,%25E9%2594%2580%25E5%2594%25AE,2,'+str(page_number)+'.html'
            page_number+=1
            if page_number>=2000:
                break
            yield scrapy.Request(url=url,dont_filter=False)
    def parse(self, response):
        post_a = response.xpath("//div[@class='el']/p/span/a/text()").getall()
        company_a=response.xpath('//div[@class="el"]/span[1]/a/text()').getall()
        salary_a=re.findall(r'<span class="t4">(.*?)</span>', response.text)[1:]
        num=0
        for i in range(len(post_a)):
            post=post_a[i]
            company=company_a[i]
            salary=salary_a[i]
            cont = Job51Item()
            cont['post'] = post
            cont['company'] = company
            cont['salary'] = salary
            yield cont


