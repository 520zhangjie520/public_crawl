import scrapy
from ..items import HappyItem
import pymongo
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
class work(scrapy.Spider ):
    name='work'
    allowed_domains=['waduanzi.com']
    def start_requests(self):
        page=1
        for i in range(10000):
            url='http://www.waduanzi.com/page/'+str(page)
            page+=1
            yield scrapy.Request(url=url)
    def parse(self, response):
        urls=response.xpath('//div[@class="item-content"]/a/@href').getall()
        for url in urls :
            print(url)
            yield scrapy.Request(url=url,callback=self.parse2,headers=headers)
    def parse2(self, response):
        ok=response.xpath('//*[@id="item-content"]/text()').getall()
        print(ok)
        count=HappyItem()
        count['data']=ok
        yield count
