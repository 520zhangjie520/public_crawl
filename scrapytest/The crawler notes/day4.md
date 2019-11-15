### 失信人

~~~markdown
1. 会有重复数据
		控制重复次数
2. 如何完整的爬取失信人的数据
		百家姓
		中国汉字大全
		import requests
import json
import MySQLdb
conn = MySQLdb.connect(host='localhost',port=3306,user='root',password='123456',charset='utf8',db='crawler')
cursor = conn.cursor()



inames='赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤'

for s in inames:
    pn = 0
    num = 0
    while num<2500:
        url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E8%A2%AB%E6%89%A7%E8%A1%8C%E4%BA%BA%E5%90%8D%E5%8D%95&cardNum=&iname=' +s+'&areaName=&pn=' + str(
            pn) + '&rn=1000&ie=utf-8&oe=utf-8&format=json&t=1571967956637&cb=jQuery110206805110476335876_1571966199119&_=1571966199192'
        pn += 10
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'Referer': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA&oq=%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598&rsv_pq=99774cf20038ef48&rsv_t=61cbMkY3TVgcuSJS6LSV0IfZNoDVH2Bpnlz8t9u86hz3xBQ5lGz7hEqT8dA&rqlang=cn&rsv_enter=1&rsv_dl=tb&inputT=5844&rsv_sug3=33&rsv_sug1=32&rsv_sug7=101&rsv_sug2=0&rsv_sug4=5844&rsv_sug=1'
        }

        res = requests.get(url=url, headers=headers)
        res = res.text[46:-2]
        res = json.loads(res)
        data = res['data'][0]['result']

        for i in data:
            # 以caseCode为主键
            try:
                sql = 'INSERT INTO shixinren VALUES (%s)'
                print(i['iname'])
                print(i['caseCode'])
                cursor.execute(sql, (i['caseCode'],))
                conn.commit()
            except:
                num+=1
~~~

### IP代理池

~~~markdown
1. 池：
		线程池进程池
		串池
		数据库连接池
2. IP代理池
		池：为了存储内容，实现一定的业务功能
		IP代理池：为了存储IP，也要实现业务功能
		
3. IP代理池的实现思路
		代理池类
			属性
				阈（yu）值
			方法
			1. 向代理池中存入IP
			2. 从代理池中取出IP
			3. 遍历数据库判断IP可用性
			4. 控制IP数量
			5. 爬取代理
~~~

~~~python
import MySQLdb
import random
import requests
from lxml import etree

# 代理池类
class IP_pool():
#   属性
    def __init__(self,limit):
#       阈（yu）值
        self.limit=limit
        self.conn = MySQLdb.connect(host='localhost',port=3306,user='root',password='123456',db='crawler',charset='utf8')
        self.cursor = self.conn.cursor()

#     方法
#     1. 向代理池中存入IP
    def save_ip(self,ip):
        if self.check_ip(ip):
            print(ip)
            sql = 'INSERT INTO crawl_ip VALUES (%s)'
            self.cursor.execute(sql, (ip,))
            self.conn.commit()

#     2. 从代理池中取出IP
    def get_ip(self):
        sql = 'SELECT * FROM crawl_ip'
        self.cursor.execute(sql)
        ips = self.cursor.fetchall()
        ip = random.sample(ips,1)[0]
        return ip

#     3. 遍历数据库判断IP可用性(定时、定量)
    def check_allip(self):
        sql = 'SELECT * FROM crawl_ip'
        self.cursor.execute(sql)
        ips = self.cursor.fetchall()
        for i in ips:
            if not self.check_ip(i[0]):
                # 当前ip不可用，删除
                sql = 'DELETE FROM crawl_ip WHERE ip=%s'
                self.cursor.execute(sql,(i[0],))
                self.conn.commit()
	
    # 检测某个ip是否可用
    def check_ip(self,ip):
        try:
            res = requests.get(url='https://www.httpbin.org/ip', proxies=eval(ip), timeout=5)
            print(res.text)
            print(ip)
        except:
            return False
        if '111.33.3' in res.text:
            return False
        return True

#     4. 控制IP数量
    def count_ip(self):
        sql = 'SELECT * FROM crawl_ip'
        ip_number = self.cursor.execute(sql)
        if ip_number<self.limit:
            return True
        return False

#     5. 爬取代理
    def crawl_ip(self):
        page_number = 1
        while self.count_ip():
            url = 'https://www.xicidaili.com/nn/'+str(page_number)
            page_number +=1
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            }
            try:
                res = requests.get(url=url, headers=headers, timeout=5).text
            except:
                continue
            ele = etree.HTML(res)
            ip = ele.xpath("//tr[@class='odd']/td[2]/text()")
            port = ele.xpath("//tr[@class='odd']/td[3]/text()")
            ip_type = ele.xpath("//tr[@class='odd']/td[6]/text()")
            for i in range(len(ip)):
                # {"type":"ip:port"}
                ip_dict = {}
                ip_dict[ip_type[i].lower()] = ip[i] + ':' + port[i]
                self.save_ip(str(ip_dict))
        self.check_allip()

if __name__ == '__main__':
    ippool = IP_pool(20)
    ippool.crawl_ip()


url = 'http://qinghuadaili.com/free/'
~~~

### 通过请求响应写人工智障

~~~python
import requests
import base64

res = requests.get('https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=FyXgFvRFACXGURXyxGneKCwz&client_secret=xE86TjIWtfoD9ckoRLdy6lq0XXzR1Fdj&',)
access_token = res.json()['access_token']

params = {
    'access_token':access_token
}

headers = {
    'Content-Type':'application/x-www-form-urlencoded'
}

url = 'https://aip.baidubce.com/rest/2.0/solution/v1/img_censor/v2/user_defined'

with open('08.jpg','rb') as r:
    img = r.read()
    img = base64.b64encode(img)

data = {
    'image':img
}

res = requests.post(url=url,params=params,headers=headers,data=data)
if res.json()['conclusion']=="合规":
    print(res.json()['conclusion'])
else:
    print(res.json()['data'][0]['msg'])
~~~

### pyecharts

~~~markdown
1. pyecharts是python中第三方的集成了生成echarts图表的一个库
2. pyecharts 0.9以上的只支持python3.5以上版本
示例
https://github.com/pyecharts/pyecharts/tree/master/example

~~~



### 作业

~~~markdown
1. 完善IP代理池
2. 通用文字识别
3. 失信人
4. 采用合适的表格
		1. 看失信人的姓氏分布
		2. 看失信人的省份分布
		3. 看失信人的年龄分布
		4. 看失信人的性别分布
		5. 看失信人的年份分布
~~~

