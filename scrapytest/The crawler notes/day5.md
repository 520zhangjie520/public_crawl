### requests的缺点

```markdown
慢
```

### 框架的分类

```markdown
1. 用法简单，功能相对单一
2. 用法复杂，功能相对强大
```

### 自己设计一个框架

```markdown
1. 请求和响应的代码需要重复写
2. 入库（保存）的代码需要重复写
3. 想办法加快速度
4. 调度的功能 --- 调度器   （对url的去重，过滤，先发哪个后发哪个）
```

![75爬虫异步框](E:\Python175\第三阶段\笔记\pic\175爬虫异步框架.png)

### scrapy

```markdown
1. 第三方的专业级的爬虫框架
	功能很强大，使用复杂
2. 协程级异步框架
3. 可以和其他的配件相结合使用
	redis，mongo，mysql
	scrapy-redis
```

### scrapy的组件

```markdown
1. Scrapy Engine 引擎
	核心，在框架中数据的流动由引擎决定
	封装好的，不要修改。
2. Scheduler ： 调度器
	从引擎接收Requests，让其进入队列，按照调度规则把Requests发送给Downloader
3. Downloader： 下载器
	发送请求，接收响应，把响应发送给Spiders
4. Spiders ： 爬虫/解析器
	解析：URL和数据
	URL再次通过引擎发送给调度器
	数据通过引擎发送给 Item Pipeline
5. Item Pipeline ： 数据管道
	入库/保存
```

![crap](E:\Python175\第三阶段\笔记\pic\scrapy.png)

### scrapy安装

```python
pip install scrapy
如果报错：
	1. vcpython  ： c++
    2. win32api : 命令模块接口
```

### 使用scrapy

```markdown
1. 创建scrapy项目
	scrapy startproject 项目名
2. cd进项目目录
	scrapy genspider example example.com
3. 编写爬虫
4. 启动项目：
	项目目录下，使用 scrapy crawl 爬虫名     命令启动
```

```python
# -*- coding: utf-8 -*-
import scrapy
from ..items import BiqugeItem

class BiqugespiderSpider(scrapy.Spider):
    name = 'biqugeSpider'
    # 允许此url之下的url发送
    # allowed_domains = ['http://www.xbiquge.la/xiaoshuodaquan/.com']
    # 起始url
    start_urls = ['http://www.xbiquge.la/xiaoshuodaquan/']
    # 第一个解析函数，start_urls发送后响应内容由parse来解析
    def parse(self, response):
        # xpath匹配
        urls = response.xpath("//div[@class='novellist']/ul/li/a/@href").getall()
        for url in urls:
            # 发送一个Request对象，发给引擎，引擎判断传来的是Request对象，给了调度器
            yield scrapy.Request(url=url,callback=self.parse1)
    # 第二个解析函数
    def parse1(self,response):
        # xpath匹配
        urls = response.xpath("//div[@id='list']//dd/a/@href").getall()
        # 列表推导式生成章节url
        urls = ["http://www.xbiquge.la"+i for i in urls]
        for url in urls:
            # 发送一个Request对象，发给引擎，引擎判断传来的是Request对象，给了调度器
            yield scrapy.Request(url=url,callback=self.parse2)
    def parse2(self,response):
        # xpath匹配
        cont = response.xpath("//div[@id='content']//text()").getall()
        # 数据简单清洗
        c = ""
        for i in cont:
            c += i.strip()
        # 实例化一个item对象
        item = BiqugeItem()
        # 往字典添加值
        item["content"] = c
        # 把item对象发送出去
        yield item
```



### scrapy编写的过程

```markdown
1. 创建项目
2. 在spider目录下创建py文件
3. 定义起始url，在parse方法里进行xpath解析响应的内容
4. 在下一个解析方法里对上一个解析的url的响应再次解析
5. 如果有数据。在items文件中，配置item字段
6. 在spider中，导入items类，进行实例化，以键值赋值的形式，给item添加值
7. 以生成器的形式 yield item对象
8. 在settings中解开ITEM_PIPELINES 的注释（配置）
9. 在pipeline中进行相应的入库（保存）操作
注意： 如果有翻页等需求，需要定义一个start_requests方法，在方法里进行操作，之后yield一个Request对象（默认指定回调函数为parse）
```

### Request的参数

```markdown
1. url : 请求的地址
2. callback : 回调函数
3. method  ： 请求方式，默认get
4. headers : 请求头
5. body  ： 发json时用 ： 不用管
6. cookies ： cookies 
7. meta  : 字典结构，包含了请求的部分信息（代理）
8. encoding : 编码格式，默认utf-8
9. priority ： 优先级。 默认即可不用改
10. dont_filter ： 是否过滤请求（已发过的）默认过滤
11. errback ： 请求失败的回调函数  （一般不用）
12. flags : 标识
```

### 作业

```
1. 51job 前程无忧  （必做）
	50000条数据。要求：字段--- 职位，公司，薪资
2. 失信人 （选做）
	50000条
```

