### 猫眼电影

~~~markdown
1. stonefont---前段中对应font_face
		第一次访问：da0 3f1
		第二次访问：442 bd4
2. 硬碰硬
		1. 下载字体文件
		2. fonttools 可以把woff文件转为xml
		3. 根据xml的字形
		4. 图像识别 OCR
		5. 通过爬虫，获得到海量的字体文件，全部存起来，通过人为观察，观察出所有的数字的点数的大概值
		6. 查看有多少pt，如果某个数字的pt数和之前存的某个数字的点数小于某个阈值
~~~

### urllib的高阶使用

- 如何加headers

~~~python
from urllib import request as ur

headers = {}

req = ur.Request(url,headers)
~~~

- 设置proxy

~~~python
# 1. 爬虫的过程中可能会被封IP
# 2. 人类行为检测

# 需要一个新的IP
	# 1. 硬实力
	# 2. 软实力
    	# 不掏钱
        #需要利用爬虫手段，从网络上爬取可用IP，并且保存起来随时使用
        #IP代理池
        # 西刺代理、快代理、等等的代理
        # 获取到的代理的格式应该为ip+port的格式
   
~~~

~~~python
from urllib import request as ur


ip = {
    'https':'117.91.131.206:9999'
}
# 构建一个控制器
handler = ur.ProxyHandler(proxies=ip)
# 构建一个opener来代替urlopen发请求
opener = ur.build_opener(handler)
res = opener.open(fullurl='http://www.httpbin.org/ip')
print(res.read())

# 1. 人为设置不符合自动化
# 2. 不花钱就意味着可用ip较少

# 为了解决这种问题
	#1. 花钱
    #2. 爬取IP，判断IP是否可用
    #3. 如果可用，入库或者存文件
~~~

- 作业

~~~markdown
爬取二十条可用IP，入库
~~~



- timeout+异常处理

~~~markdown
1. 超时设置
		1. 服务器炸了
		2. 链接失效
		3. 网速太慢
2. 如果出现了以上情况
		报500错误
		没有获取到需要的数据
		pass掉
3. 可以在urlopen中设置超时，单位为秒，如果超时的话，抛出timeout异常
4. timeout必须搭配try使用
~~~

~~~python
from urllib import request as ur

try:
    res = ur.urlopen(url='http://www.google.com', timeout=1)
    print(res.read().decode())
except:
    print('超时啦')
~~~

- 设置cookie

~~~markdown
1. 强制登录
		1. 在网页上手动登录，copy用户的登录后的cookie，发请求的时候携带
		2. 利用爬虫，发送登录请求，响应会携带一个登录后的cookie，再次发请求的时候，携带返回的cookie即可
2. 维持用户的登录状态
~~~

~~~python
from urllib import request as ur

headers = {
    'Cookie': 'lianjia_uuid=dc928208-c794-4502-b9be-0b781d28a2ed; _smt_uid=5dafa5ff.422ecbda; UM_distinctid=16df6206dd8380-08b3d35fdaa6af-3d375b01-1fa400-16df6206dd9275; _jzqc=1; _jzqy=1.1571792384.1571792384.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6.-; _jzqckmp=1; sajssdk_2015_cross_new_user=1; _ga=GA1.2.1622434487.1571792386; _gid=GA1.2.1198365456.1571792386; select_city=110000; all-lj=dafad6dd721afb903f2a315ab2f72633; _qzjc=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216df620708d189-0e2d0328bb9ef9-3d375b01-2073600-16df620708f112%22%2C%22%24device_id%22%3A%2216df620708d189-0e2d0328bb9ef9-3d375b01-2073600-16df620708f112%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22sousuo%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; digv_extends=%7B%22utmTrackId%22%3A%2221583074%22%7D; lianjia_ssid=2d61e66e-43fa-4615-9e5c-ac2ac0f1c6df; _qzja=1.393681390.1571792390872.1571792390872.1571799189166.1571792390872.1571799189166.0.0.0.2.2; _qzjto=2.2.0; _jzqa=1.3982488718051555300.1571792384.1571792384.1571799189.2; CNZZDATA1253477573=251136261-1571788242-%7C1571799042; CNZZDATA1254525948=480895923-1571790095-%7C1571795495; CNZZDATA1255633284=1792714560-1571790103-%7C1571795503; CNZZDATA1255604082=1275483693-1571788185-%7C1571798985; _jzqb=1.1.10.1571799189.1; _qzjb=1.1571799189166.1.0.0.0; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYzkwMjNlODZlZDhkMGIxYWI2MjIxNDU4NmZmN2VmNWJhYWI4MTcwMGJjNTViZmE3MzU4MjAyNjVmMjBlMTM1OTI4NWIzMTQ4ODNlZjk2ODVmNzhhYzEwMDVkYmNjYzdhMmZiMTAzZmFhZjc3Yzg5ZGNmN2YxMTQzYzU5NDA0YWJiY2NiM2NiN2Y1NDVkMWI4Yjc1ZDc1NzZmOWNjZTQ1NTU1OWE1OWU3MjlkZDZjOTRjNGFkNTI1ZjFlOTA4MjU4MDIyNzk3YmVkNDU0YTFjYjc4MTQ0NDUzMjlhMDg2NjZhMzdkZjI1ZDlmNTZlNjg5NTUzMmU2NDBlMjBkY2NkYmE5OGE1MzYyYWY4ODgxNWU4N2IzNDY2MzU4ZjA3MmY0ZWZmMTRhZDUxNDJjNDIxNjI1N2UyODgzNmFmMmY2Y2FcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiM2FhNDQ4ZWVcIn0iLCJyIjoiaHR0cHM6Ly9iai5saWFuamlhLmNvbS8/dXRtX3NvdXJjZT1iYWlkdSZ1dG1fbWVkaXVtPXBpbnpodWFuJnV0bV90ZXJtPWJpYW90aSZ1dG1fY29udGVudD1iaWFvdGltaWFvc2h1JnV0bV9jYW1wYWlnbj1zb3VzdW8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1'
}

req = ur.Request(url='http://www.httpbin.org/cookies',headers=headers)
res = ur.urlopen(req).read()
print(res.decode())
~~~

- urlretrieve

~~~python
# 提供的一个爬取图片的方法
from urllib import request as ur

# res = ur.urlopen(url='https://p0.meituan.net/movie/223c3e186db3ab4ea3bb14508c709400427933.jpg').read()
# with open('1.jpg','wb') as w:
#     w.write(res)

ur.urlretrieve(url='https://p0.meituan.net/movie/223c3e186db3ab4ea3bb14508c709400427933.jpg',filename='2.jpg')
~~~

- 练习

~~~markdown
爬百度图片---随意
要求100张
~~~

- 要求

~~~markdown
1. 允许作业完不成
2. 把思路全部写下来
~~~



















