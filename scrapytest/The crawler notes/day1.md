### j爬虫

~~~markdown
1. 薪资高
2. 要求低
爬虫：需要web的技术，大数据，数据挖掘数据分析，AI
~~~

### 爬虫是什么

~~~markdown
英文名(spider)蜘蛛，网络机器人，网络蜘蛛等等
爬虫是一段能够自动化的从网上大批量获取数据的程序
自动化：代码一次写好不用管
大批量数据：至少是千万级以上
程序：代码
想象成一个大蜘蛛觅食
爬取数据
以数据为导向（不择手段）
~~~

### 为什么需要爬虫？

~~~markdown
1. 自动化获取数据，提高效率，减少了人力（省钱）
2. 给大数据提供数据支持
3. 给数据分析提供数据支持
4. 给人智提供数据集
5. 百度、谷歌、搜狐...搜索引擎
6. 好就业，薪资高，要求低
~~~

### 爬虫的分类

~~~markdown
1. 通用爬虫（大而全）
		搜索引擎
		功能强大，搜索面广
		百度、搜狐、搜狗、谷歌、必应、yahoo、360
		贵
2. 聚焦爬虫（小而精）
		focus
		又叫主题爬虫
		针对某一主题（所需要的主题）进行针对性的爬取
3. 增量式爬虫
		增量：针对更新
		更新
		只要区分新老数据就行了
~~~

### 君子协定

~~~markdown
1. 在网站的根目录下输入/robots.txt，即可查看君子协定
		user-agent: 用户标识，标识了用户的系统版本，浏览器版本等
		规定了君子协定后，从技术上可以爬，从原则问题上不能爬
		公司说了算
		如果规定了有些内容不能爬，但是爬了并且商用盈利了，对方会追究责任，并且君子协定会作为证据出庭。
2. sitemap:
		需要浏览量的网站
		站点地图：为了方便搜索引擎更快的收录自己的网站
~~~

### 爬虫的原理

~~~markdown
1. 以数据为导向，不择手段
2. 请求---响应
~~~

![求响](E:\Python175\第三阶段\笔记\pic\请求响应.png)







### 请求头

![12分](E:\Python175\第三阶段\笔记\pic\F12分析.png)









![头](E:\Python175\第三阶段\笔记\pic\头.png)

### 请求类型

~~~markdown
1. get
	明文，参数以?拼接的形式传参
2. post
	密文，参数以form表单的形式传参
3. delete
	删除请求，权限一般不开放，百度网盘
4. put
	上传请求，百度网盘
~~~

### 第一个爬虫程序

~~~markdown
不择手段
请求响应
1. 发请求，使用urllib请求库
		python内置的请求库
		1. urllib的request方法中的urlopen发送请求
		2. 需要的参数为url
		3. 获得到响应之后，需要先read()，观察得到的是什么数据，然后对数据进行处理
		字符串
2. urlopen
		open是打开的意思
		开启网络传输流
~~~

~~~markdown
1. get()
		urllib.request.urlopen(url)
2. post()
		urllib.request.urlopen()		
~~~

~~~python
# post请求
from urllib import request as ur
import urllib.parse

data = urllib.parse.urlencode(data).encode()
req = ur.Request(url='https://www.iqianyue.com/mypost',data=data)
print(req)
res = ur.urlopen(req)
print(res.read().decode())
~~~

### 笔趣阁压缩流

~~~python
from urllib import request as ur
import urllib.parse
import gzip

url = 'http://www.xbiquge.la/xiaoshuodaquan/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',

}

req = ur.Request(url=url,headers=headers)
res = ur.urlopen(req)
s = res.read()
# gzip在python中可以处理压缩流数据，gzip中的decompress可以进行解压缩，compress可以进行压缩
print(gzip.decompress(s).decode())
~~~

### xpath语法

~~~markdown
1. xpath是python中的一个第三方解析库
	lxml 
	pip install lxml
2. from lxml import etree
		1. 构建一个element对象
			ele = etree.HTML(html字符串)
		2. 对element对象进行xpath解析
			ele.xpath(xpath语法)
~~~

~~~markdown
1. //根节点下的所有元素
2. []谓语
3. @属性
4. /当前节点下的元素
5. 内置函数
		text()
~~~

### 笔趣阁

~~~python
# 请求响应
# 不择手段
# 以数据为导向
import urllib.parse
from urllib import request as ur
import json
import pickle
#
# res = ur.urlopen(url='http://www.xbiquge.la/xiaoshuodaquan/')
# print(res.read())

# data = {
#     'name':'xiangui',
#     'pass':'xiangui'
# }
# data = urllib.parse.urlencode(data).encode()
# print(data)
# res = ur.urlopen(url='http://www.iqianyue.com/mypost',data=data)
# print(res.read())

# 'http://www.baidu.com?pass=xiangui&name=xiangui'
# data = urllib.parse.urlencode(data).encode()
# req = ur.Request(url='https://www.iqianyue.com/mypost',data=data)
# print(req)
# res = ur.urlopen(req)
# print(res.read().decode())
import gzip
from lxml import etree

url = 'http://www.xbiquge.la/xiaoshuodaquan/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',

}

req = ur.Request(url=url,headers=headers)
res = ur.urlopen(req)
s = res.read()

try:
    s = gzip.decompress(s).decode()
except:
    s = s.decode()

ele = etree.HTML(s)
urls = ele.xpath("//div[@class='novellist']/ul/li/a/@href")
book_name = ele.xpath("//div[@class='novellist']/ul/li/a/text()")
for url in urls:
    ind = urls.index(url)
    book = book_name[ind]
    req = ur.Request(url=url, headers=headers)
    res = ur.urlopen(req)
    s = res.read().decode()
    ele = etree.HTML(s)
    zhangjie_urls = ele.xpath("//div[@id='list']//dd/a/@href")
    zhangjie_name = ele.xpath("//div[@id='list']//dd/a/text()")

    for zhangjie_url in zhangjie_urls:
        index = zhangjie_urls.index(zhangjie_url)
        zhangjie = zhangjie_name[index]
        req = ur.Request(url='http://www.xbiquge.la'+zhangjie_url, headers=headers)
        res = ur.urlopen(req)
        s = res.read().decode()
        ele = etree.HTML(s)
        cont = ele.xpath("//div[@id='content']//text()")
        c = zhangjie+'\n'
        for j in cont:
            c += j.strip()
        c += '\n'
        with open(book+'.txt','a+',encoding='utf-8') as w:
            w.write(c)

import MySQLdb

conn = MySQLdb.connect(host='localhost',port=3306,user='root',password='123456',charset='utf8')
cursor = conn.cursor()

sql = 'INSERT INTO 表 VALUE (%s,%s,%s)'
cursor.execute(sql,(值1，值2，值3))
conn.commit()
conn.close()
~~~



~~~markdown
作业
	1. 笔趣阁搞定
		5本
	2. 猫眼电影top100
		要求：入库
		字段：电影名、英文名、类型、上映地点、电影市场、上映时间、用户评分、累计票房
查作业：
		组长查，截止到九点
晨讲：李思毅，余伦，尚龙飞
~~~















