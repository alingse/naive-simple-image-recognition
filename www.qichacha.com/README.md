#这是最基本简单的一个
##
### 破解简单 验证码
#### 介绍
1. 图片
	 
	如图 ：    ![](./test_data/400.jpg) ![](./test_data/401.jpg) ![](./test_data/402.jpg)

     还有更简单的一些验证码种类 略去

2. 算法
	
    K-means. 就是计算 相似度，排名高的前K个里面最多的一个


这里是全套的制作流程，快速的话，大概需要 半小时。

当然，一些东西还是要改的，

 + 一个是 下载图片 <br> 修改 getimg.py
 + 一个是 二值化 <br> 修改 doimg.py
 + 一个是 验证码分割 的个数 <br> 修改 makeyzm.py <br> 修改 yzm.py
 + 一个是 验证码的 字符种类数目 <br> 修改 makeyzm.py <br> 修改 yzm.py

#### 流程

1. 下载图片

	**getimg.py**
	 
2. 二值化

	**doimg.py**
	
	二值化要视具体情况而定，最后，字白底黑即可。
	
	程序里面两个，一个是基于 是否 彩色，一个是 RGB 阈值
 
3. 制作

	**makeyzm.py**
	  
         程序会自动按照 yzm.py 的分割来分割，
	<br> 之后在屏幕打印该字符，输入对应的 字符即可，当然也可以修改代码，用图片来展示。
	<br> 程序会依据 char_ max ，char_count，每个字符收集 相应数目的样例。
4. 测试
	**testyzm.py**  

5. 使用

	 **./training_data_select** <br>
		**yzm.py**	<br>
		**doimg.py** <br>

	这三个可以用在程序中去 使用了


运行样例
``
python getimg.py
python doimg.py
python makeyzm.py
python testyzm.py
``