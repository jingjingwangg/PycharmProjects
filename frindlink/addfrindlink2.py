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
#case3:名称为空
driver.find_element_by_xpath(".//*[@id='main-content']/section/div[1]/div/section/header/a").click() #新增按钮
time.sleep(3)
driver.find_element_by_id("name").send_keys("")
driver.find_element_by_id("url").send_keys("http://www.baidu.com")
driver.find_element_by_id("rank").send_keys("1")
driver.find_element_by_xpath(".//*[@id='addModal']/div/div/div[3]/button[2]").click()
t1=driver.find_element_by_xpath(".//*[@id='signupForm']/div[1]/div/label").text
if t1==u"这是必填字段":
    print("请输入名称")
else:
    print("提交成功")
driver.quit()