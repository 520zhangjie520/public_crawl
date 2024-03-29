### 滑块验证码

- 思路

~~~markdown
1. 鼠标移动到滑块按钮，出现图像 
2. 点到滑块按钮，出现按钮以及缺口
3. 把滑块移动到缺口位置
		需要知道缺口距离图片最左边的长度
4. 松开鼠标
~~~

![rop过](E:\Python175\第三阶段\笔记\pic\crop过程.jpg)





- pixel

~~~markdown
1. 获得所有像素点，生成两个列表
		1. 有序无缺口图像的像素列表
		2. 有序有缺口图像的像素列表
2. 对所有像素点进行比对
		所有像素点对象:
			R:R值
			G:G值
			B:B值
		if abs(R1-R2)>10 or abs(G1-G2)>10 or abs(B1-B2)>10（杨明潮猜想）（10指的是色差）
		噪点：
			为了防止噪点，控制杨明潮猜想中的色差。
3. 获取到距离后，按着滑块，滑动过该距离即可。
		
~~~

![动流](E:\Python175\第三阶段\笔记\pic\滑动流程.jpg)





~~~markdown
1. 获取图片，获取到两张图片，一张为乱序无缺口，一张为乱序有缺口
2. 使用pillow的crop()方法，将两张图片各分割为52张图片
3. 按照前端给的相应坐标，对52张图片进行合并(merge())
4. 使用pillow的pixel()方法进行像素块遍历
5. 对每个像素块的RGB值进行比对，如果有一个值大于50,缺口位置就是在该像素。
6. 进行人类行为模拟滑动
		1. 滑动的轨迹为y=-x^2(x>0)
		2. 滑动的速度为变速（加/减）运动，但不能匀，不能为0
		3. 快到终点时进行减速
		4. 到达终点时进行纠错行为模拟
				划过终点一段距离，然后再回来
~~~

- 滑块验证码的硬处理

~~~markdown
1. js加密
~~~

- JS加密的解决方法

~~~markdown
1. 读懂JS
2. 运行JS
		1. 使用Python代码模拟JS的加密逻辑进行加密
				美团酒店：沙河如家900/晚（JS处理）
						function(num){
                            num = num-700
                            return num
						}
						浏览器显示：200/晚
				def suan(num):
					return num-700
		2. 直接运行JS
				找到加密所在的地方，然后进行JS运行
3. 无界面浏览器
~~~

- pyexecjs

~~~markdown
1. 第三方提供的一个python运行js的一个库

~~~

~~~python
import execjs


f = execjs.compile("""
function f(num) {
    return num-700
};
""")
print(f.call('f',900))

~~~

- 动态自定义字体

~~~markdown
1. 不要硬刚：
		不择手段，找其他地方，看有没有相同数据
		开发周期相对较短
		头发掉的较少
2. 方法：
		1. 一定会传来一个字体文件（woff/tff）
		2. 下载下来该文件，使用百度字体平台进行读取
		3. fonttools
		4. 手动创建一个字典
				每个数字和每个数字的点数的对应关系
				{1：30,2:35,3:45,4:40,5:50}
				查一下数字的点数
				这个数字的点数和哪个最接近
3. OCR：
		图像识别
~~~

![of](E:\Python175\第三阶段\笔记\pic\woff.png)



![8](E:\Python175\第三阶段\笔记\pic\8.jpg)



- APP采集

~~~markdown
相同之处：请求--响应
不同之处：APP响应都是json
思路：
1. 在电脑上安装一个安卓模拟器，在模拟器上安装所需的app
2. 使用抓包工具拦截APP请求，将wifi设置为抓包工具的代理，配置完抓包工具，需要重启
3. 使用代码模拟APP发送的请求，获得响应并解析
~~~



- 作业

~~~markdown
1. 复习
2. 今天代码过一遍
3. app采集抖音短视频，20个
~~~

