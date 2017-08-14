# Python in CodeWars

---

### 第一题：编写函数toJadenCase(string) ，完成以下测试

```python
quote = "How can mirrors be real if our eyes aren't real"
test.assert_equals(toJadenCase(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")
```

**LIFE**

```python
def toJadenCase(string):
    l = string.split(" ")       # 以空格为切分参考，将字符串切分成多个单词字符串组成的list
    r = ""                      # 声明空白的字符串变量r
    for i in l:                 # 处理每个单词 
        r += i.capitalize()     # 首字母大写函数capitalize()
        r += " "                # 单词末尾加上空格符
    r = r[0:len(r)-1]           # 去掉整句话末尾的空格符
    return r
```


**DREAM**

```python
def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())
------------------------------------------------------------
import string

def toJadenCase(NonJadenStrings):
    return string.capwords(NonJadenStrings)
------------------------------------------------------------
import string
toJadenCase = string.capwords
------------------------------------------------------------
from string import capwords as toJadenCase
```

**知识点**

1. 切分字符串函数.split( ) 函数

2. 首字母大写函数.capitalize( )

3. 字符串切分

4. [字符串处理参考](http://www.jb51.net/article/47956.htm)

   ​

---

### 第二题：编写函数iq_test( )满足以下测试：

```python
Test.assert_equals(iq_test("2 4 7 8 10"),3)
Test.assert_equals(iq_test("1 2 2"), 1)
```

**LIFE**

```python
def iq_test(numbers):
    #your code here
    l = numbers.split(" ")
    o, e, s, p, z= 0
    for i in l:
        z = i
        if z / 2 == 0:
            o += 1
            s = i
        else:
            e += 1
            p = i
    if o == 1:
        return s + 1
    else:
        return p + 1
```



---

### 第三题：编写函数series_sum( )满足一下测试：

```python
Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
  
SeriesSum(1) => 1 = "1.00"
SeriesSum(2) => 1 + 1/4 = "1.25"
SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"

Test.assert_equals(series_sum(1), "1.00")
Test.assert_equals(series_sum(2), "1.25")
Test.assert_equals(series_sum(3), "1.39")
```

**LIFE**

```python
def series_sum(n):
    # Happy Coding ^_^
    i = 1
    sum = 0
    while i <= (3*n-2):
        sum += 1/i
        i += 3
    return '%.2f' % sum    # 保留小数点后两位并且返回str类型
        
```

**DREAM**

```python
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
```

**知识点**

1. '%.2f' % sum 保留小数点后两位并且返回str类型
2. 关于保留小数点后几位的操作参考[这里](http://www.cnblogs.com/Raymon-Geng/p/5784290.html)
3. str.format() [官方文档](https://docs.python.org/3.5/library/stdtypes.html?highlight=str%20format#str.format)、[个人总结](http://www.cnblogs.com/hongten/archive/2013/07/27/hongten_python_format.html)



---

### 第四题：编写函数countBits( )满足一下测试：

```python
Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in the binary representation of that number.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

test.assert_equals(countBits(0), 0);
test.assert_equals(countBits(4), 1);
test.assert_equals(countBits(7), 3);
test.assert_equals(countBits(9), 2);
test.assert_equals(countBits(10), 2);
```

**LIFE**

```python

```

**DREAM**

```python

```

**知识点**

1. '%.2f' % sum 保留小数点后两位并且返回str类型
2. 关于保留小数点后几位的操作参考[这里](http://www.cnblogs.com/Raymon-Geng/p/5784290.html)
3. str.format() [官方文档](https://docs.python.org/3.5/library/stdtypes.html?highlight=str%20format#str.format)、[个人总结](http://www.cnblogs.com/hongten/archive/2013/07/27/hongten_python_format.html)

