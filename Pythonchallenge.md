# Pythonchallenge

---

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

### 5.