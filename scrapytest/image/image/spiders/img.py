import scrapy
import json
from ..items import  ImageItem
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1572403264182_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&sid=&word=%E6%96%97%E5%9B%BE&f=3&oq=doutu&rsp=1'
}
class Image(scrapy.Spider ):
    name = 'image'
    def start_requests(self):
        page=30
        name=input('请输入你搜索图片的名字')
        num=input('请输入你想要的图片页数，一页为30张')
        for i in range(int(num) ):
            url = "http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%96%97%E5%9B%BE&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word="+str(name)+"&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=" + str(
                page ) + "&rn=30&gsm=&1572403318477="
            page+=30
            yield scrapy.Request(url=url,headers=headers)
    def parse(self, response):
        count=ImageItem()
        datas=response.text
        datas=json.loads(datas)
        urls = []
        try:
            for data in datas["data"]:
                try:
                    urls.append(data['hoverURL'])
                except:
                    pass
            count['image_urls'] = urls
            yield count
        except:
            pass


