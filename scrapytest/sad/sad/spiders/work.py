# -*- coding: utf-8 -*-
import scrapy

from ..items import  SadItem
class WorkSpider(scrapy.Spider):
    name = 'work'
    def start_requests(self):
        url = "http://www.xbiquge.la/xiaoshuodaquan/"
        yield scrapy.Request(url)

    def parse(self, response):
        list_url = response.xpath('//div[@class="novellist"]//a/@href').getall()
        for url in list_url:
            yield scrapy.Request(url, callback=self.jiexi)
    def jiexi(self,resp):
        item = SadItem()
        title = resp.xpath("//h1/text()").getall()[0]
        author = resp.xpath("//div[@id='info']/p[1]/text()").getall()[0]
        new_author = author.split("：")[-1]
        item['title'] = title
        item['author'] = new_author
        yield item
