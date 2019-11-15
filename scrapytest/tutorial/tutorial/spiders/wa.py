import scrapy
import re
import json
from ..items import  TutorialItem
class StockSpider(scrapy.Spider):
    name = 'work'

    def start_requests(self):
        num = 1572609512747
        for i in range(100000):
            url = 'http://59.push2.eastmoney.com/api/qt/ulist.np/get?fid=f3&pi=0&pz=40&po=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&fields=f14,f12,f13,f2,f3,f4,f6,f104,f105,f106&np=1&cb=jQuery112406661588105858278_1572609512748&secids=100.TOP40%2C100.AS51%2C100.ATX%2C100.BFX%2C100.BVSP%2C100.TSX%2C100.PX%2C100.FCHI%2C100.HEX%2C100.GDAXI%2C100.AEX%2C100.ASE%2C100.SENSEX%2C100.ICEXI%2C100.JKSE%2C100.N225%2C100.KS11%2C100.ISEQ%2C100.MIB%2C100.KLSE%2C100.MXX%2C100.NZ50%2C100.KSE100%2C100.WIG%2C100.RTS%2C100.OMXSPI%2C100.STI%2C100.CSEALL%2C100.IBEX%2C100.SSMI%2C100.SET%2C100.TWII%2C100.FTSE%2C100.DJIA%2C100.NDX%2C100.SPX%2C100.VNINDEX&_='+str(num)
            num+=1
            yield scrapy.Request(url)

    def parse(self, response):
        res=response.text[42:-2]
        res=eval(res )["data"]["diff"]
        count=TutorialItem()
        count["data"]=res
        print(res)
        yield count


