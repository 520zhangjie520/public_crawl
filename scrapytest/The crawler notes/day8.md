### MongoDB

```markdown
mysql : 关系型数据库
	基于磁盘：持久化
redis : 非关系型数据库
	基于内存：块
mongoDB：
	介于关系型数据库和非关系型数据库之间的数据库。MongoDB支持的数据类型比较松散，可以是json，Bson(二进制的json)，他可以存储一些比较复杂的数据，他可以实现关系型数据库的部分功能。
特点：
	1. 高性能
		查询和写入基于内存的
	2. 易部署
		安装方便（部署方便） 1. 下载一个msi的文件，一路点击下一步即可。2.配置好的文件
	3. 易使用
		在查询时和关系型数据库比较像（可以有条件）
```

### 安装mongo

```markdown
1. 可以上网自行下载
	https://www.mongodb.com/download-center   找到对应的版本自行下载
2. 提供了一个安装包
配置过程：
	1. 在某个盘符下创建一个文件夹
	2. 在这个文件夹中创建两个文件夹，一个是mongoDB，另一个是mongodata
	3. mongoDB是存放mongo组件的文件夹
	   mongodata是存放相关数据的文件夹
	4. 进入mongoDB的bin目录下，在cmd命令行里敲如下指令：mongod.exe --dbpath mongodata的路径
     5. 把bin目录加入到环境变量中
     6. 另开一个黑窗口，输入mongo即可进入数据库
```

### mongo操作

```markdown
1. 数据库操作
	show dbs  : 展示所有的数据库
	db : 展示当前所指向的数据库
	use 数据库：  使用某个数据库
	db.dropDatebase() : 删库，删除当前指向的数据库
2. 集合操作
	增加一个集合：
		db.createCollection('集合名字')
	查看所有集合：
		show collections
	往集合里插入数据：
		db.集合名.insert(json串)
	查看集合中的数据：
		db.集合名.find()
	往集合里插入多条数据：
		db.集合名.insertMany([json1,json2,json3,...])
		json内容可以不一致，不等长，都可以
	修改：
		db.集合名.update(查询条件，修改后)
3. 查询操作
		1. db.集合名.find([查询条件]) ： 查询出所有的json
		2. db.集合名.findOne(【查询条件】): 默认查询第一个
		3. db.集合名.find().count()  查询集合中共有多少条数据
		4. db.集合名.find().limit(前几条) 查询前几条数据
	比较运算符
		大于：$gt: granter than  
		小于：$lt: less than
		大于等于：$gte : equal
		小于等于:$lte 
		不等于：$ne: not equal
		等于：$eq  equal
		查询所有年龄大于20的信息
		db.集合名.find({条件字段:{筛选规则:值}})
	逻辑运算符
		逻辑与：and
		逻辑或：or
		逻辑非：not
	# 查询所有年龄在25和30之间的信息
	db.persons.find( {$and: [{age:{$gt:25}},{age:{$lt:30}}]})
	# 查询所有年龄不是大于25的信息
	db.persons.find({age:{$not:{ $gt:25}}})
	# 双重否定的
	db.persons.find({age:{$not:{$not:{$gt:25}}}})
```

### pymongo

```markdown
pip install pymongo 【==版本号】
类似mysqlclient第三方库，是对mongo操作的第三方库
mongodb的默认端口号：27017
```

```python
import pymongo

# 建立一个链接
conn = pymongo.MongoClient("mongodb://localhost:27017")

# 选择使用哪个数据库
mydb = conn['hero']

# 使用哪个集合
myset = mydb['name']
#增
# myset.insert([{"name":"曹建平","sex":"爷们","age":66},{"sex":"娘们","age":66}])
# myset.insert_one({"name":"土星","sex":"老爷们","age":"100"},{"name":"星星","sex":"老爷们","age":"100"})
# myset.insert_many([{"文广":"胖子","_id":"1"},{"谢春":"感谢春天"}])
#删
# myset.drop()  # 删除整个集合的数据
# mydb.drop_collection('hello') # 删除集合
# conn.drop_database("haha")
# myset.remove('1')
#改
# myset.update({"文广":"胖子"},{"文广":"瘦子"})  # 查找条件，修改的内容
# myset.update({"_id":"1"},{"文广":"瘦子"})
# myset.update({"_id":"1"},{"文广":"瘦候子","sex":18})
# myset.update({"_id":"1"},{'$set':{"sex":"爷们"}}) #只修改某一个数据
# #查
# datas = myset.find()
# for data in datas:
#     print(data)
# from lxml import etree
# import requests
# url = "http://lol.duowan.com/hero/"
# res = requests.get(url).text
# html = etree.HTML(res)
# names = html.xpath("//div[@class='champion_name']/text()")
# list1 = []
# for name in names:
#     list1.append({"_id":name,"name":name})
# myset.insert(list1)
# datas = myset.find()
# for data in datas:
#     print(data)
```

```markdown
1. 失信人   10w条
2. 智联（选做） 10w条
存mongodb
复习redis操作
```
