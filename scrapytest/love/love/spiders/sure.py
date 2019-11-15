import scrapy

from ..items import LoveItem
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
class app(scrapy.Spider):
    name='love'
    def start_requests(self):
        url='http://www.zhenai.com/jiaoyou'
        yield scrapy.Request(url=url ,headers=headers  )
    def parse(self, response):
        urls=response.xpath('//*[@id="app"]/article/dl/dd/a/@href').getall()
        for i in urls :
            for j in range(6):
                url=i+'/'+str(j)
                print(url)
                yield scrapy.Request(url=url,callback=self.parse1 )
    def parse1(self,response):
        name=response.xpath('//div[@class="content"]/div[1]/a/span/text()').getall()
        age=response.xpath('//div[@class="content"]/div[1]/span/text()').getall()
        sex=response.xpath('//div[@class="content"]/div[2]/text()').getall()
        li=[]
        for i in range(len(name) ):
            li.append([name[i],age[i],sex[i]])
        if li==[]:
            pass
        else:
            count = LoveItem()
            count['data']=li
            yield count


