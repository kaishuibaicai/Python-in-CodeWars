### 错误记录

---

#### 1.在使用Chromedriver的时候由于版本过低引起的错误。[参考](https://stackoverflow.com/questions/40373801/python-selenium-webdriver-session-not-created-exception-when-opening-chrome)

```python
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/code wars/Python-in-CodeWars/softwareTestLearning/baidu.py", line 5, in <module>
    driver = webdriver.Chrome()
  File "C:\Python27\lib\site-packages\selenium\webdriver\chrome\webdriver.py", line 65, in __init__
    keep_alive=True)
  File "C:\Python27\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 73, in __init__
    self.start_session(desired_capabilities, browser_profile)
  File "C:\Python27\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 121, in start_session
    'desiredCapabilities': desired_capabilities,
  File "C:\Python27\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 173, in execute
    self.error_handler.check_response(response)
  File "C:\Python27\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 164, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: u'session not created exception\nfrom unknown error: Runtime.executionContextCreated has invalid \'context\': {"auxData":{"frameId":"2868.1","isDefault":true},"id":1,"name":"","origin":"://"}\n  (Session info: chrome=59.0.3071.86)\n  (Driver info: chromedriver=2.22.397933 (1cab651507b88dec79b2b2a22d1943c01833cc1b),platform=Windows NT 10.0.10586 x86_64)' 
```

需要升级版本，[下载](http://chromedriver.storage.googleapis.com/index.html?path=2.24/)后配置PATH环境变量



System.setProperty("webdriver.chrome.driver", "C:\Python27\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe");



---

#### 2.如何在Windows下同时使用py2 和 py3 [参考](https://python.freelycode.com/contribution/detail/139)

#### 如何同时在Windows下安装Anaconda2 和 Anaconda3[参考](http://blog.csdn.net/Infin1te/article/details/50445217)



---

#### 3.Windows环境下的编码错误问题：

```Python
UnicodeDecodeError: 'ascii' codec can't decode byte 0xcb in position 37
: ordinal not in range(128)
```

找到错误提示的文件并打开，加上如下代码：

```python
if sys.getdefaultencoding() != 'gbk':
    reload(sys)
    sys.setdefaultencoding('gbk')
    default_encoding = sys.getdefaultencoding()
```

或定位出错的位置加上如下代码：

```Python
try:
    出错代码
except UnicodeEncodeError:
    pass
```

[参考](https://stackoverflow.com/questions/4237898/unicodedecodeerror-ascii-codec-cant-decode-byte-0xe0-in-position-0-ordinal)