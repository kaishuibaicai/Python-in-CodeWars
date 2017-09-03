#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://mail.qq.com")

print ('Before login===========')

print (driver.title)
print (driver.current_url)

driver.switch_to.frame(driver.find_element_by_id("login_frame")).find_element_by_id("u").clear()
driver.switch_to.frame(driver.find_element_by_id("login_frame")).find_element_by_id("u").send_keys("272251416")
