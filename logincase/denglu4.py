#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("http://b.anfubaoxian.cn")
driver.find_element_by_name("username").clear()
driver.find_element_by_name("password").clear()
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("Afb123")
driver.find_element_by_xpath("html/body/div[1]/form/div/button").submit()
time.sleep(3)
t=driver.find_element_by_xpath(".//*[@id='adminContent']/header/div[2]/ul/li[7]/a/span").text
if t==u"管理员":
    print("pass")
else:
    print("error")
driver.quit()