## 源码

### 文件(图片)下载

```markdown
1. 在settings里配置
	IMAGES_URLS_FIELD = "image_urls"  # image_urls 是默认字段
	IMAGES_STORE =   文件保存路径
	解开pipeline的注释。配置ITEM_PIPELINES  为
	scrapy.pipelines.images.ImagesPipeline
	如果是没有headers，cookies的时候直接这么配置即可
2. item中设置字段名为image_urls
3. 编写spider，注意item值是一个字典，键名为image_urls，值是url组成的列表
4. 在pipeline里面配置。（可选的）
	如果需要请求带参数，就需要继承自ImagesPipeline，重写get_media_requests，把参数放进Request里面
以上内容，自行调控。
还有分页等操作，需要在pipeline中定义额外的分页逻辑（重写方法）
代码在day7的项目里哦
```

### 日志

```markdown
是否启用日志：
settings里面配置：
	LOG_ENABLED = False    默认是True
日志级别：
	向上兼容
	LOG_LEVEL = "日志等级"
	CRITICAL  严重的错误，可能引起程序崩溃
	ERROR： 一般错误
	WARNING: 警告
	INFO： 基本信息
	DEBUG： 程序调试信息
	
主动使用日志：
	import logging
	logging.日志等级（小写）(msg="日志信息")
```

### 断点续传

```markdown
在settings里面设置
JOBDIR = "路径"   目录是持久化的目录
注意：不是什么时候都能成功，一般跟多个元素，比如电脑配置等有关
所以配置断点续传，最好还是手动
```

### Scrapy的断点续传:调度器的内存队列和磁盘队列

```markdown
1. 内存队列：在内存中的容器（保存url的）
	优点：快
	缺点：不能持久化
2. 磁盘队列：在磁盘中的容器（保存url的）
	优点：可以持久化
	缺点：慢
Scrapy的内存队列和磁盘队列不能同时使用。默认使用的时内存队列，我们可以通过JOBDIR判断讲内存队列转为磁盘队列。
```

### Scheduler

![hedule](E:\Python175\第三阶段\笔记\pic\Sheduler.png)

### CrawlSpider

```markdown
针对的就是所有内容都可以在html页面上获取到的网页，相对逻辑比较少
1. 导包
	from scrapy.spiders import CrawlSpider，Rule
2. 书写spider类，需要继承CrawlSpider类
3. 编写Rule规则，定义a标签对应的回调函数，以及跟进（注意回调函数名字是个字符串）
4. 最后在响应的回调函数处理response即可
缺点: 不能处理ajax请求，不能处理复杂的反爬。
优点：使用简便
```

```python
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class xuanhuan(CrawlSpider):
    name = "xuanhuan"
    rules = (
        Rule(link_extractor=LinkExtractor(restrict_xpaths="//*[@id='newscontent']/div[1]/ul/li/span[1]"),callback='parse1'),  # 抽取规则1，当前页的a标签的href属性
        Rule(link_extractor=LinkExtractor(restrict_xpaths="//a[@class='next']"),follow=True)  # 抽取规则2，下一页的
    )
    def start_requests(self):
        url = "http://www.xbiquge.la/xuanhuanxiaoshuo/"
        yield scrapy.Request(url)
    def parse1(self, response):
        print(response.xpath("//h1/text()").getall())
```

### 作业

```
1. 珍爱网
	字段名： 姓名，性别，年龄     （多多益善）
	3万条
2. 挖段子网
	5万条存数据库
```

