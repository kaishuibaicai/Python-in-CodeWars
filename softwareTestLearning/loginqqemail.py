#coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://mail.qq.com")

print ('Before login===========')

print (driver.title)
print (driver.current_url)

driver.find_element_by_id("u").clear()
driver.find_element_by_id("u").send_keys("272251416")
