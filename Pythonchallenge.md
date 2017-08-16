# Pythonchallenge

1.修改URL

```python
2 ** 38
>>>274877906944
```

2.根据密码图翻译一段话：

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

Ascll码表:

![Ascll码表](http://ww1.sinaimg.cn/large/bd31b54fgy1fikua0wh7cj20w30mn7e8.jpg)

[**string.maketrans()**](http://www.runoob.com/python3/python3-string-maketrans.html)的使用参考

