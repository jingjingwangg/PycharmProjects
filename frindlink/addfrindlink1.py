#encoding:utf-8
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
    print("登录成功")
else:
    print("登录失败")
driver.find_element_by_xpath(".//*[@id='basic-home']/span").click()
time.sleep(4)
#case2:单击取消按钮
driver.find_element_by_xpath(".//*[@id='main-content']/section/div[1]/div/section/header/a").click()#新增按钮
time.sleep(5)
driver.find_element_by_xpath(".//*[@id='addModal']/div/div/div[3]/button[1]").click()#取消按钮
time.sleep(3)
t1=driver.find_element_by_xpath(".//*[@id='main-content']/section/div[1]/div/section/header/a").text
if t1==u"新增":
    print("取消，关闭弹窗")
else:
    print("弹窗未关闭")
time.sleep(3)
driver.quit()