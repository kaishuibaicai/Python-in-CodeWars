# Pythonchallenge

---

[TOC]



### 0.修改URL

```python
2 ** 38
>>>274877906944
```

---

### 1.根据密码图翻译一段话：

```python
#g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

K --> M
O --> Q
E --> G

def key(a):
  	n = ""
	for l in a:
		if ord(l) >= 65 and ord(l) <= 120:    #ord()字母转ascll码对应数字
        	n += chr(ord(l)+2)				  #chr()ascll码数字转对应字母
        elif ord(l) >= 121 and ord(l) <= 122:
        	n += chr(ord(l)-24)
        else:
          	n += l
     return n
输入：
key("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
输出：  
"i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."
根据提示：
>>>intab = 'abcdefghijklmnopqrstuvwxyz'
>>>outtab = 'cdefghijklmnopqrstuvwxyzab'
>>>trantab = str.maketrans(intab, outtab)
>>>str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
>>>print(str.translate(trantab))
接着翻译url上的"map"得到"ocr",打开下一个界面
```

- Ascll码表:

![Ascll码表](http://ww1.sinaimg.cn/large/bd31b54fgy1fikua0wh7cj20w30mn7e8.jpg)

- [**string.maketrans()**](http://www.runoob.com/python3/python3-string-maketrans.html)的使用参考
- [**官方答案**](http://wiki.pythonchallenge.com/index.php?title=Level1:Main_Page)

---

### 2.打开页面后，得到以下提示：recognize the characters. maybe they are in the book, but MAYBE they are in the page source.

遂单击右键打开检查，查看页面源，果然发现如下字符串：

```python
<!--
find rare characters in the mess below:
-->
<!--
%%$@_$^__#)^)&!_+]!*@&^}@[@%]()%+$&[(_@%+%$*^@$^!+]!&_#)_*}{}}!}_]$[%}@[{_@#_^{*
.........................特别多的字符，这里省略....................................
}!)$]&($)@](+(#{$)_%^%_^^#][{*[)%}+[##(##^{$}^]#&(&*{)%)&][&{]&#]}[[^^&[!#}${@_(
#@}&$[[%]_&$+)$!%{(}$^$}*
-->

def key(a):
  	n = ""
	for l in a:
		if ord(l) >= 65 and ord(l) <= 122:    #满足是字母则添加到新的字符串里。
          	n += l
     return n
  
由于该字符串由许多换行，因此以上程序处理不了，改用按行读取文件的形式。首先将整个页面的源码保存成ocr.txt

file = open("ocr.txt")
n = ""
while 1:
    line = file.readline()
    if not line:
        break
    for l in line:
        if l == "-":           # 识别<--与-->开始换行 更好看出筛选出来的信息
            n += "\n"
        elif ord(l) >= 65 and ord(l) <= 90:
            n += l
        elif ord(l) >= 97 and ord(l) <= 122:
            n += l
print (n)
  
得到equality，打开下一个页面
```

- [**按行读取文件**](http://www.cnblogs.com/xuxn/archive/2011/07/27/read-a-file-with-python.html)参考
- [**官方答案**](http://wiki.pythonchallenge.com/index.php?title=Level2:Main_Page)

---

### 3.One small letter, surrounded by **EXACTLY** three big bodyguards on each of its sides.

![3题图](http://www.pythonchallenge.com/pc/def/bodyguard.jpg)

```python
该小写字母两边均被三个大写字符包围，图中可以看出物体高低看出：小大大大[小]大大大小
import re
file = open("4.txt")
n = ""
while 1:
    line = file.readline()
    if not line:
        break
    for l in line:
        if ord(l) >= 65 and ord(l) <= 90:
            n += l
        elif ord(l) >= 97 and ord(l) <= 122:
            n += l
patt = """[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]"""
a = re.findall(patt,n)
print (a)
得到结果：['l', 'i', 'n', 'k', 'e', 'd', 'l', 'i', 's', 't']
```

- [**Python中re的match、search、findall、finditer区别**](http://blog.csdn.net/djskl/article/details/44357389)
- [python里的正则表达式](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000)


---

### 4.打开页面后是一个提示：

提示是“linkedlist.php”，更改url后，是一张图，图片可点击。点击后又是提示“and the next nothing is 44827”，更改url：nothing=44827。又是一个提示“and the next nothing is 45439”。不出预料，又是一个更改url的提示，并且他还嘲讽我说：手会累的。遂：

```Python
import urllib.request
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
while 1:
    h= str(urllib.request.urlopen(url).read())
    a = re.findall(r'the next nothing is (\d+)',h)
    if a[0] is None:
        print (h)
        break
    print (h)
    print (a[0])
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+a[0]
```

通过小爬虫的到最后一个数字是：16044，打开页面是这么一句话：“Yes. Divide by two and keep going.”，额，还要继续：“and the next nothing is 25357”。到了“82682”这里出现了**误导数字**，需要屏蔽“There maybe misleading numbers in the text. One example is 82683. Look only for the next nothing and the next nothing is 63579”。需要加强爬虫的屏蔽功能，在正则表达式前加上**”the next nothing is “**。最终打开的网页名是：peak.html.

- [**urllib2**](http://python.jobbole.com/86247/)

---

### 5.页面打开如下图所示

![5](http://www.pythonchallenge.com/pc/def/peakhell.jpg)

提示信息：pronounce it.   页面源代码有这样的提醒：peak hell sounds familiar ?    我真的不知道像什么，所有谷歌了一下：[pickle](http://python.usyiyi.cn/translate/python_278/library/pickle.html), python的一个对象序列化模块。代码里还有一个banner.p的source，打开后是一对待处理的数据。

```python
from urllib.request import urlopen
import pickle
data = pickle.load(urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
for line in data:
    print("".join([k * v for k, v in line]))
```

得到：

```python
              #####                                                                      ##### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
      ###      ####   ###         ###       #####   ###    #####   ###          ###       #### 
   ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     #### 
  ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   #### 
 ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  #### 
 ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  #### 
####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  #### 
####           ####     ####   ##########    ####     ####  ####     #### ##############  #### 
####           ####     ####  ###    ####    ####     ####  ####     #### ####            #### 
####           ####     #### ####     ###    ####     ####  ####     #### ####            #### 
 ###           ####     #### ####     ###    ####     ####  ####     ####  ###            #### 
  ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   #### 
   ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    #### 
      ###     ######    #####    ##    #### ######    ###########    #####      ###      ######
data的值：
[[(' ', 95)], [(' ', 14), ('#', 5), (' ', 70), ('#', 5), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 6), ('#', 3), (' ', 6), ('#', 4), (' ', 3), ('#', 3), (' ', 9), ('#', 3), (' ', 7), ('#', 5), (' ', 3), ('#', 3), (' ', 4), ('#', 5), (' ', 3), ('#', 3), (' ', 10), ('#', 3), (' ', 7), ('#', 4), (' ', 1)], [(' ', 3), ('#', 3), (' ', 3), ('#', 2), (' ', 4), ('#', 4), (' ', 1), ('#', 7), (' ', 5), ('#', 2), (' ', 2), ('#', 3), (' ', 6), ('#', 4), (' ', 1), ('#', 7), (' ', 3), ('#', 4), (' ', 1), ('#', 7), (' ', 5), ('#', 3), (' ', 2), ('#', 3), (' ', 5), ('#', 4), (' ', 1)], [(' ', 2), ('#', 3), (' ', 5), ('#', 3), (' ', 2), ('#', 5), (' ', 4), ('#', 4), (' ', 3), ('#', 3), (' ', 3), ('#', 4), (' ', 4), ('#', 5), (' ', 4), ('#', 4), (' ', 2), ('#', 5), (' ', 4), ('#', 4), (' ', 3), ('#', 3), (' ', 5), ('#', 3), (' ', 3), ('#', 4), (' ', 1)], [(' ', 1), ('#', 3), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 3), (' ', 4), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 6), ('#', 4), (' ', 2), ('#', 4), (' ', 1)], [(' ', 1), ('#', 3), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 10), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 7), ('#', 3), (' ', 2), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 2), (' ', 3), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 7), ('#', 3), (' ', 2), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 10), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 14), (' ', 2), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 4), ('#', 4), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 12), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 5), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 12), ('#', 4), (' ', 1)], [(' ', 1), ('#', 3), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 5), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 12), ('#', 4), (' ', 1)], [(' ', 2), ('#', 3), (' ', 6), ('#', 2), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 4), ('#', 4), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 3), (' ', 6), ('#', 2), (' ', 3), ('#', 4), (' ', 1)], [(' ', 3), ('#', 3), (' ', 4), ('#', 2), (' ', 3), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 11), (' ', 3), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 4), ('#', 3), (' ', 4), ('#', 2), (' ', 4), ('#', 4), (' ', 1)], [(' ', 6), ('#', 3), (' ', 5), ('#', 6), (' ', 4), ('#', 5), (' ', 4), ('#', 2), (' ', 4), ('#', 4), (' ', 1), ('#', 6), (' ', 4), ('#', 11), (' ', 4), ('#', 5), (' ', 6), ('#', 3), (' ', 6), ('#', 6)], [(' ', 95)]]

```

- [**pickle.load**](http://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p21_serializing_python_objects.html)
- [**"".join() **](http://www.w3school.com.cn/jsref/jsref_join.asp)

---

### 6.打开后是这样的：

![6](http://www.pythonchallenge.com/pc/def/channel.jpg)

遂打开源代码，

```html
<html> <!-- <-- zip -->
<head>
  <title>now there are pairs</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<img src="channel.jpg">
<br/>
```

第一行有“zip”字样，将URL更改成channel.zip, 就把压缩包解压了。里面全是txt文件，又是"the next nothing is ..." , 里面有的readme文件， 打开说：”welcome to my zipped list.hint1: start from 90052 hint2: answer is inside the zip“

```python
import re
url = 'channel/90052.txt'
file = open(url)
while 1:
    file = open(url)
    line = file.readline()
    a = re.findall(r'Next nothing is (\d+)',line)
    if a[0] is None:
        print (line)
        break
    print (line)
    print (a[0])
    url = 'channel/'+a[0]+'.txt'
```

程序到46145.txt 就停下来到了，打开一看提示：**Collect the comments.**

根据参考，原来是每个文件还有注释，也需要保存在一个列表里，更改代码如下：

```python
import re, zipfile

f = zipfile.ZipFile("channel/channel.zip")
url = '90052.txt'
comments = []
while 1:
    line = f.read(url).decode("utf-8")
    a = re.search(r'Next nothing is (\d+)',line)
    comments.append(f.getinfo(url).comment.decode("utf-8"))
    if a is None:
        print (line)
        break
    print (line)
    url = a.group(1)+'.txt'
print ("".join(comments))
```

得到如下图案：

```
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
```

打开hockey.html后，得到：“it's in the air. look at the letters.”，再看上面的图案，里面的字母是：“oxygen”

- [**Python 的 zipfile 处理**](http://python.jobbole.com/81519/)



---

### 7.