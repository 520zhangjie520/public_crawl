import scrapy
import time
from ..items import FaItem
class a(scrapy.Spider ):
    name = "work"
    def start_requests(self):
        for i in range(100,1761331620000):
            for j in range(1,11):
                url="http://13.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112408145561628676579_1572743762373&pn="+str(int(j))+"&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:90+t:3&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f124,f107,f104,f105,f140,f141,f207,f222&_="+str(int(i))
                try:
                    print(i,j)
                    time.sleep(5)
                    yield scrapy.Request(url=url,)
                except:
                    pass

    def parse(self,response):
       res = response.text[42:-2]
       res = eval(res)["data"]["diff"]
       count = FaItem()
       count["data"] = res
       yield count