## 扒源码

```markdown
1. 如何发请求和接收响应
2. 发请求需要携带的参数
3. headers 
4. cookies
5. 代理
6. get，post
7. 处理响应
	筛选： 正则，xpath，css选择器
8. 如何保存
```

### 昨天自己配置的内容

```markdown
1. Spider   2. Items  3.Pipeline   4.settings
 settings : 君子协议
		配置pipeline
 最大连接数
```

### settings

![etting](E:\Python175\第三阶段\笔记\pic\settings.png)

### Item

![tem](E:\Python175\第三阶段\笔记\pic\items.png)

### Pipelines

![ipeline](E:\Python175\第三阶段\笔记\pic\pipelines.png)

### 配置UA的方式

```markdown
1. 在setting的USER_AGENT 里面配置全局UA
2. 在spider里面自己配置一个UA
3. 在settings中配置DEFAULT_REQUEST_HEADERS全局headers
```

### 使用post请求

```python
使用FormRequest方法请求
class YuanmaspiderSpider(scrapy.Spider):
    name = 'yuanmaSpider'
    # allowed_domains = ['yuanma.com']
    # start_urls = ['https://www.httpbin.org/headers']
    def start_requests(self):
        data = {"name":"wwww","pass":"1234"}
        url = 'https://iqianyue.com/mypost'
        yield scrapy.FormRequest(url=url,formdata=data)

    def parse(self, response):
        print(response.text)
```

### cookie

```markdown
在spider里面设置cookie即可。
注意： 需要以键值对的形式传入
cookies = {
    "BIDUPSID":"B61DDFF966B8DBCF28E001DBF794F91B",
    "PSTM":"1571651769",
    "BAIDUID":"5D8DE9DB36F3CF6A063C25A0FA3AEBB6:FG=1"
           }
```

### 代理

```markdown
在meta里面写入代理
代理的格式：字符串
'http/https://ip：端口号'
meta['proxy'] = 代理
```

### Spider

![pide](E:\Python175\第三阶段\笔记\pic\spider.png)

### 中间件

![间](E:\Python175\第三阶段\笔记\pic\中间件.png)

### 随机UA

```markdown
1. 在setting中解开DOWNLOADER_MIDDLEWARES  注释，配置好中间件
2. 里面设置好随机的UA组成的列表，注意只是值
3. 在中间件中使用随机选择的方式，在process_request这个方法里给request.headers['User-Agent'] 赋值随机选择好的ua
4. 正常发请求即可
```

### 随机代理

```markdown
1. 在setting中解开DOWNLOADER_MIDDLEWARES  注释，配置好中间件
2. 里面设置好随机的代理组成的列表，注意代理格式是字符串
3. 在中间件中使用随机选择的方式，在process_request这个方法里给request.meta['proxy'] 赋值随机选择好的代理
4. 正常发请求即可
```

```python
from scrapy import signals
from .settings import UA,PROXY
import random
class UAMiddleware(object):
    def process_request(self, request, spider):
        ua = random.choice(UA)
        request.headers['User-Agent'] = ua
        return None

class Proxy(object):
    def process_request(self,request,spider):
        proxies = random.choice(PROXY)
        request.meta['proxy'] = proxies
        return None
```

### 响应

```markdown
1. text 文本数据
2. body 二进制流数据
3. xpath() 做解析  获取：getall() 或者extract()
4. meta  可以获取代理，mete里存放的时服务返回给我们的信息
5. headers  响应头
```

### 作业

```
协同开发
	字段：
		招聘岗位，学历要求，工作经验，薪资
	抓取的数据量：组员*5万
管培生分配任务
	大街网，宁夏人才网，服装人才网，各省人才网...
```

