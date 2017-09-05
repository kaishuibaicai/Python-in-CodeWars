#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("http://mail.qq.com")
sleep(2)
print ('Before login===========')
driver.implicitly_wait(10)
print (driver.title)
print (driver.current_url)

driver.switch_to.frame(driver.find_element_by_id("login_frame")).find_element_by_name("u").clear()
driver.switch_to.frame(driver.find_element_by_id("login_frame")).find_element_by_name("u").send_keys("272251416")
