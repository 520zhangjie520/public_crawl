

### urllib的问题

~~~markdown
1. 写起来特麻烦
		urllib.request.urlopen(url).read().decode()
		read().decode()一直在重复的
2. 一旦需要伪装请求头，IP等
		handler--->opener--->opener.open()
~~~

### 封装urllib

~~~markdown

~~~

### Requests高级请求库

~~~markdown
1. 基于urllib编写的HTTP请求库
		reqeusts的底层使用urllib
2. 更加pythonic
		python化，使用起来更加人性化
3. 是目前企业开发中，最常用的请求库
		urllib基本不用
		urllib就像张无忌学太极拳
4. 第三方
~~~

### Requests的相关函数

~~~markdown
1. get(url, params=None, **kwargs)
		发送一个get请求
		url：统一资源定位符
		params：可选参数，可以是字典
		**kwargs：关键字参数
2. post(url, data=None, json=None, **kwargs)
		发送一个post请求
		url：统一资源定位符
		data：post请求所需要的数据
		json：post请求所需要的json数据
		**kwargs：关键字参数
3. request(method, url, **kwargs)
~~~

- get

~~~python
import requests


res = requests.get(url='http://www.baidu.com')
print(res.text)
~~~

- post

~~~python
import requests

data = {
    'name':'123',
    'pass':'123'
}

res = requests.post(url='http://www.iqianyue.com/mypost',data=data)
~~~



### Response对象的属性

~~~markdown
1. response对象常用的属性
		1. text:指的是返回响应内容的字符串形式(默认为utf-8解码)
		2. content:指的是返回响应内容的二进制形式
		3. encoding:自动识别当前响应的编码格式
		4. status_code:返回当前响应的状态码
		5. cookies:返回一个cookieJar对象，用来存放响应返回的cookie
		6. elapsed:返回当前的响应时间
		7. url:返回当前的url
		8. history:返回历史记录
		9. json():直接输出转为字典的json数据
		10. headers:返回当前请求的响应头
~~~

~~~python
# import requests
#
# url = 'https://www.baidu.com/s'
#
# params = {
#     'wd':'xiangui',
#     'tn':'baidu'
# }
#
# res = requests.get(url=url,params=params)
# print(res.history)



import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0'
}

res = requests.get(url='http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&force=&pn=60&rn=30&gsm=&1571886338082=',headers=headers)
print(res.headers)
~~~



### 高阶使用

- headers

~~~python
import requests

headers = {
    'User-Agent':'xiangui'
}

res = requests.get(url='http://www.httpbin.org/headers',headers=headers)
print(res.text)
~~~

- cookies

~~~python
import requests

# cookies = {
#     'xiangui':'nan',
#     'aqian':'nv',
#     'wangxing':'nan',
#     'lekai':'nv'
# }

headers = {
    'Cookie':'xiangui=nan;aqian=nv;lekai=nan;wangxing=nan'
}

res = requests.get(url='https://www.httpbin.org/cookies',headers=headers)
print(res.text)
~~~

- ip代理

~~~python
import requests

# 存放100个ip，每一次发完请求都random一个ip
ips = {
    'http':'11.2.3.2:8080'
}

try:
    res = requests.get(url='https://www.httpbin.org/ip', proxies=ips, timeout=1)
    print(res.text)
except:
    print('超时啦')
~~~

### 断点续传

~~~markdown
1. 爬取的过程中因为种种原因（1. 网络 2. 封IP 3. 火灾 4. 地震）,会中断当前数据的爬取
2. 为了中断后能够继续爬取，采用断点续传

需要知道：
	在哪儿断的
	1. 目前在爬哪本书
	2. 目前爬到该书的第几章
	断点信息需要几条？
scrapy
		自动断点
		JOB_DIR = '断点目录'
~~~

~~~python
import requests
from lxml import etree
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',password='123456',charset='utf8',db='crawler',port=3306)
cursor = conn.cursor()

def get_book_url():
    book_url,cont_url=get_duandian()
    print(book_url,cont_url) # pythonic
    url = 'http://www.xbiquge.la/xiaoshuodaquan/'
    res = requests.get(url=url).text
    ele = etree.HTML(res)
    urls = ele.xpath("//div[@class='novellist']/ul/li/a/@href")
    if book_url!='1' and cont_url!='1':
        book_number = urls.index(book_url)
        for i in urls[book_number:]:
            get_cha_url(i, cont_url)
    else:
        for i in urls:
            get_cha_url(i)

def get_cha_url(url,cont_url=''):
    res = requests.get(url=url).content.decode()
    ele = etree.HTML(res)
    cha_urls = ele.xpath("//div[@id='list']/dl/dd/a/@href")
    book_name = ele.xpath("//h1/text()")[0]
    print(book_name)
    print(cha_urls)
    print(cont_url)
    if cont_url == '':
        for j in cha_urls:
            get_content(j,book_name,url)
    else:
        cont_number = cha_urls.index(cont_url)
        for i in cha_urls[cont_number + 1:]:
            get_content(i, book_name, url)

def get_content(cont_url,book_name,book_url):
    res = requests.get(url='http://www.xbiquge.la'+cont_url).content.decode()
    ele = etree.HTML(res)
    cont = ele.xpath("//div[@id='content']/text()")
    cont_name = ele.xpath("//h1/text()")[0]
    with open(book_name+'.txt','a+',encoding='utf-8') as w:
        w.write(cont_name+'\n')
        for i in cont:
            w.write(i)
        w.write('\n')
    duandian(book_url,cont_url)

def duandian(book_url,cont_url):
    global conn
    global cursor
    sql = 'UPDATE biquge_duandian SET book_url=%s,cont_url=%s'
    cursor.execute(sql,(book_url,cont_url))
    conn.commit()

def get_duandian():
    global conn
    global cursor
    sql = 'SELECT * FROM biquge_duandian'
    cursor.execute(sql)
    data = cursor.fetchone()
    return data

if __name__ == '__main__':
    get_book_url()
~~~



### 作业

~~~markdown
1. 封装适合自己的urllib
2. 改善自己的ip爬取
3. 使用requests重写笔趣阁，采用结构化编程的方式，必须写类（不要求写断点）
4. 百度失信人，需要爬取人名、执行法院、省份、案号、生效法律文书确定的义务、被执行人的履行情况、失信被执行人行为具体情形、发布时间，两张表
~~~

