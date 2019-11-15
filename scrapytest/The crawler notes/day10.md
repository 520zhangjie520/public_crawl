### 人人网（requests）

~~~markdown
1. 登录
2. 访问首页，获得到推荐好友的所有url，url入库，并且状态码为0
3. 从数据库中取出一个url（未访问的），同时把该url的状态改为1
4. 向魏星的页面发送请求，获得到魏星的个人隐私并且保存，同时获得到最多22个url，把url入库并且状态改为0
~~~

~~~markdown
1. url表
		url(主键)    status
		魏星           1
		hehe           0
		haha           0
		heihei         0
2. data表
		姓名
~~~

- 解决验证码

~~~markdown
1. 图像识别
		王牌
		爬虫的尽头OCR
2. 硬实力
		掏钱
~~~

~~~python
import requests
from lxml import etree
import MySQLdb
from chaojiying import chaojiying_check

conn = MySQLdb.connect(host='localhost',port=3306,user='root',password='123456',db='crawler',charset='utf8')
cursor = conn.cursor()
cookies = {
    'Cookie': 'jebe_key=9ef043d4-4d6e-4080-9f10-b420f02262ab%7Cc06fd7b330d1b34a3b663a70fd4e85c3%7C1572321519485%7C1%7C1572321521609; anonymid=k2bg3n2mso4hkr; _r01_=1; depovince=GW; JSESSIONID=abcJ-kjRKEh209JlYh04w; ick_login=7a809358-148c-49e2-a961-de09da87adbc; t=b249c9b4498418bb3bc51dbc4540db660; societyguester=b249c9b4498418bb3bc51dbc4540db660; id=969805440; xnsid=cbe084a5; ver=7.0; loginfrom=null; wp_fold=0; jebecookies=38f304c3-301a-498d-9942-889d11ca8832|||||; XNESSESSIONID=5a90698f9ccf; jebe_key=9ef043d4-4d6e-4080-9f10-b420f02262ab%7Cc9648fadd971497f6415b29ba7925b4e%7C1572848841070%7C1%7C1572848845096'
}

# 1. 登录
# 2. 访问首页，获得到推荐好友的所有url，url入库，并且状态码为0
# 3. 从数据库中取出一个url（未访问的），同时把该url的状态改为1
# 4. 向魏星的页面发送请求，获得到魏星的个人隐私并且保存，同时获得到最多22个url，把url入库并且状态改为0

# 访问某人的页面
def view_detail(url):
    res = requests.get(url=url,cookies=cookies)
    ele = etree.HTML(res.text)
    print(url)
    try:
        name = ele.xpath("//title/text()")[0].strip()
    except:
        change_status(url)
        return
    print(name)
    save_data(name)
    if name != '人人网 - 验证码':
        change_status(url)
        urls = ele.xpath("//div[@id='footprint-box']/ul/li/a/@namecard")
        save_url(urls)
    else:
        #处理验证码
        # print(res.text)
        img_url = ele.xpath("//div[@class='optional']/img/@src")[0]
        img = requests.get(url=img_url,cookies=cookies)
        with open('code.jpg','wb') as w:
            w.write(img.content)
        check_code(chaojiying_check(img.content),url)

def check_code(code,url):
    check_url = 'http://www.renren.com/validateuser.do'
    code = code.get('pic_str')
    print(code)
    data = {
        'icode': code,
        'submit': '继续浏览',
        'id': url.split('/')[3],
        'requestToken': '1845850427',
        '_rtk': '39c66f95'
    }

    requests.post(url=check_url,data=data,cookies=cookies)

# 把用户信息入库
def save_data(data):
    sql = 'INSERT INTO renren_data values (%s)'
    cursor.execute(sql,(data,))
    conn.commit()

# 修改url状态为1
def change_status(url):
    sql = 'UPDATE renren_url SET status=1 where url=%s'
    cursor.execute(sql,(url,))
    conn.commit()

# 保存爬下来的url
def save_url(urls):
    for url in urls:
        try:
            sql = 'INSERT INTO renren_url VALUES (%s,%s)'
            cursor.execute(sql, ('http://www.renren.com/'+url+'/profile', "0"))
            conn.commit()
        except:
            pass


# 从数据库中获取第一个status为0的url
def get_url():
    sql = 'SELECT url FROM renren_url where status=%s'
    cursor.execute(sql,("0",))
    url = cursor.fetchone()[0]
    view_detail(url)

# 处理全新的url
if __name__ == '__main__':
    while True:
        get_url()
~~~

~~~python
# 超级鹰
#!/usr/bin/env python
# coding:utf-8

import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


def chaojiying_check(im):
    chaojiying = Chaojiying_Client('haha', 'heihei', '902126')	#用户中心>>软件ID 生成一个替换 96001
    return chaojiying.PostPic(im, 1902)												#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()

~~~

- 作业

~~~markdown
1. 人人网
2. 商标网（注意尺度）
3. 网易云音乐-我已经敢想你（8000条）
		手段不限
~~~

