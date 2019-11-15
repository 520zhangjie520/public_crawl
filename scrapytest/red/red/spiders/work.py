import scrapy

from ..items import  RedItem
class wa(scrapy.Spider):
    name = 'work'

    def start_requests(self):
        url = 'https://www.lianjia.com/city/'
        yield scrapy.Request(url=url)

    def parse(self, response):
        urls = response.xpath("//div[@class='city_province']/ul/li/a/@href").getall()
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse1)

    def parse1(self,response):
        url = response.xpath('/html/body/div[1]/div/div[3]/div/ul/li[2]/a/@href').getall()
        yield scrapy.Request(url=url[0],callback=self.par )

    def par(self,response):
        honse_pig = response.xpath('//div[@class="content__list--item--main"]/p/text()[5]').getall()
        honse_for = response.xpath('//div[@class="content__list--item--main"]/p/text()[7]').getall()
        honse_monny = response.xpath('//div[@class="content__list--item--main"]/span/em/text()').getall()
        count=RedItem()
        li=[]
        for i in range(len(honse_pig) ):
            li.append([honse_pig[i],honse_for[i],honse_monny[i]])
        if li==[]:
            pass
        else:
            count["data"]=li
            yield count
