#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("http://b.anfubaoxian.cn")
driver.find_element_by_name("username").clear()
driver.find_element_by_name("password").clear()
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("Afb12")
driver.find_element_by_xpath("html/body/div[1]/form/div/button").submit()
time.sleep(3)
t=driver.find_element_by_xpath("html/body/div[1]/form/div/button").text
if t==u"登录":
    print("pass")
else:
    print("error")
driver.quit()