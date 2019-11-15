### 网易云音乐评论

~~~python
import requests
import MySQLdb
import json
conn = MySQLdb.connect(host='localhost',port=3306,user='root',password='123456',db='crawler',charset='utf8')
cursor = conn.cursor()
url = 'http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearchDG.html'

i = 1
while True:
    data = {
        'page': '1',
        'rows': '1000000000',
        'annNum': str(i),
        'annType': '',
        'tmType': '',
        'coowner': '',
        'recUserName': '',
        'allowUserName': '',
        'byAllowUserName': '',
        'appId': '',
        'appIdZhiquan': '',
        'bfchangedAgengedName': '',
        'changeLastName': '',
        'transferUserName': '',
        'acceptUserName': '',
        'regName': '',
        'tmName': '',
        'intCls': '',
        'fileType': '',
        'totalYOrN': 'false',
        'appDateBegin': '',
        'appDateEnd': '',
        'agentName': '',
    }
    i+=1
    # data = dict([line.split(": ",1) for line in data.split("\n")])
    # headers = dict([line.split(": ",1) for line in headers.split("\n")])
    print(data)
    res = requests.post(url=url, data=data)
    for item in json.loads(res.text)['rows']:
        try:
            print(item['tm_name'])
            sql = 'INSERT INTO sb VALUES (%s)'
            cursor.execute(sql, (item['reg_num'],))
            conn.commit()
        except:
            continue
~~~

### Jieba

~~~markdown
1. 第三方的中文分词工具
2. 把网易云中的所有评论全部进行分词，并且放到一个列表中
~~~

~~~python
import jieba
import MySQLdb

conn = MySQLdb.connect(host='localhost',port=3306,user='root',password='123456',db='crawler',charset='utf8')
cursor = conn.cursor()

sql = 'select common from wyyyy'
cursor.execute(sql)
commons = cursor.fetchall()
fenci_commens = []
for common in commons:
    fenci_commens+=jieba.lcut(common[0].split('：',1)[1])
~~~

### 词云

~~~markdown
wordcloud
~~~

~~~python
import wordcloud

w = wordcloud.WordCloud(font_path='E:\Python175\第三阶段\代码\day11\simkai.ttf',scale=5,mask=img,background_color='white')
w.generate(s)
w.to_file('我已经敢想你.jpg')
~~~

### 爬取策略

~~~markdown
1. 深度优先
2. 广度优先
~~~

- 深度优先（DFS）

~~~markdown
深度优先搜索算法（英语：Depth-First-Search，简称DFS）是一种用于遍历或搜索树或图的算法。 沿着树的深度遍历树的节点，尽可能深的搜索树的分支。当节点v的所在边都己被探寻过或者在搜寻时结点不满足条件，搜索将回溯到发现节点v的那条边的起始节点。整个进程反复进行直到所有节点都被访问为止。
~~~

![F](E:\Python175\第三阶段\笔记\pic\DFS.jpg)

~~~python
# 深度优先思路
深度优先类
	属性
    1. 容器
    方法
    1. 存
    2. 取
~~~

~~~python
import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}
#深度优先类
class DFS():
#	属性
    def __init__(self):
#    1. 容器
        self.dfs = []
        self.crawled = []
#    方法
#    1. 存
    def save_url(self,url):
        if url not in self.crawled:
            self.dfs.append(url)

#    2. 取
    def get_url(self):
        url = self.dfs.pop()
        self.crawled.append(url)
        return url

class Crawl():
    def __init__(self):
        self.dfs = DFS()


    def crawler(self):
        url = 'http://www.xbiquge.la/'
        self.dfs.save_url(url)
        while True:
            try:
                new_url = self.dfs.get_url()
                print(new_url)
                res = requests.get(url=new_url, headers=headers,timeout=3)
                ele = etree.HTML(res.content.decode())
                urls = ele.xpath("//a/@href")
                print(ele.xpath("//title/text()"))
                for i in urls:
                    if self.check_url(i):
                        self.dfs.save_url(i)
                print(self.dfs.dfs)
            except:
                pass

    def check_url(self,url):
        if (url.startswith('http://') or url.startswith('https://')) and not url.endswith('.exe'):
            return True
        else:
            return False


if __name__ == '__main__':
    crawl = Crawl()
    crawl.crawler()

~~~

- BFS

~~~markdown

~~~



![F](E:\Python175\第三阶段\笔记\pic\BFS.jpg)



~~~python
import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}
#广度优先类
class BFS():
#	属性
    def __init__(self):
#    1. 容器
        self.bfs = []
        self.crawled = []
#    方法
#    1. 存
    def save_url(self,url):
        if url not in self.crawled:
            self.bfs.append(url)

#    2. 取
    def get_url(self):
        url = self.bfs.pop(0)
        self.crawled.append(url)
        return url

class Crawl():
    def __init__(self):
        self.bfs = BFS()


    def crawler(self):
        url = 'http://www.baidu.com'
        self.bfs.save_url(url)
        while True:
            try:
                new_url = self.bfs.get_url()
                print(new_url)
                res = requests.get(url=new_url, headers=headers,timeout=3)
                ele = etree.HTML(res.content.decode())
                urls = ele.xpath("//a/@href")
                print(ele.xpath("//title/text()"))
                for i in urls:
                    if self.check_url(i):
                        self.bfs.save_url(i)
                print(self.bfs.bfs)
            except:
                pass

    def check_url(self,url):
        if (url.startswith('http://') or url.startswith('https://')) and not url.endswith('.exe'):
            return True
        else:
            return False


if __name__ == '__main__':
    crawl = Crawl()
    crawl.crawler()
~~~

### 作业

~~~markdown
协同开发，以组为单位，采用scrapy-redis
爬猎聘，数据量要求（组员人数*10W）
~~~

