### 分布式爬虫架构

~~~markdown
1. 设计好所有的组件的数量（按功能划分，一个功能对应一个组件）
2. 组件间的通信
3. 设计好分布之间的关系（主从、主备、全主）
4. 需要特殊处理的组件
~~~

### 分布式爬虫架构的设计思路

~~~markdown
需要进行分布的是请求响应的过程---下载器
~~~

![布式爬虫架](E:\Python175\第三阶段\笔记\pic\分布式爬虫架构.jpg)



- 写两个进程

~~~markdown
1. print A
2. print B
~~~



- requests-html

~~~markdown
1. python的第三方请求库
2. 作者：是requests的作者
3. 为了解决某些js加密应运而生的一个库
~~~

- 如何学习新的框架或库

~~~markdown
1. get请求
2. post请求
3. 如何获得响应
4. 响应的相关方法
5. 如何解析响应
~~~

### aiohttp

~~~markdown
asyncio http
第三方的异步http请求库
~~~

~~~markdown
pip install aiohttp
~~~

- 为什么要用异步？

~~~markdown
1. 我们平常使用requests是同步的，一旦发生网络阻塞，后面的程序全都不执行
2. 由于GIL锁的原因，Python对于多线程的支持很差。
3. 使用了异步就可以更合理的安排资源了。
~~~

~~~python

~~~

