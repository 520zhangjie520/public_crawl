### 分布式

```markdown
1. 多个进程（多个电脑/终端）共同去完成一个大的任务（需求）
	1. 多个进程做同样的事
	2. 相同的事不能重复
2. 解决进程通信的问题
```

### 我们用的分布式

```markdown
简陋的分布式
	每个人负责不同的主体界面，把数据汇总
scrapy做分布式
```

### scrapy-redis分布式框架

```markdown
 scrapy-redis是scrapy框架基于redis数据库的组件,用于scrapy项目的分布式开发和部署。
 安装：pip install scrapy-redis
 一定要安装redis数据库
 一路下一步就行，傻瓜式安装
```

![crapy-redis分布](E:\Python175\第三阶段\笔记\pic\scrapy-redis分布式.png)

### 如何配置

```markdown
1. settings里面配置：
	REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
	SCHEDULER = 'scrapy_redis.scheduler.Scheduler'  # 调度器配置（所在的路径）
	DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'  # 配置去重策略：指纹去重
	
	SCHEDULER_PERSIST = True  # 持久化存储url,断点续传
2. 正常书写执行scrapy程序即可
```

### 作业

```markdown
1. 设计一个比scrapy-redis更优秀的框架
	画图把功能画出来，需要说明解释
2. scrapy-redis  租房信息网   数据量不限
3. 股票信息（股票）
	股票代码，股票名称，最新价，成交额，市盈率
4. 电影天堂（信息）  1万部
```

