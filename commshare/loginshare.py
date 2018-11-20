from selenium import  webdriver
import time
class openweb():
    def openweb(self,url):
        global dr
        dr=webdriver.Firefox()
        dr.get(url)
    def close(self):
        dr.quit()
    def login001(self,username,password):
        dr.find_element_by_name("username").send_keys(username)
        dr.find_element_by_name("password").send_keys(password)
        dr.find_element_by_xpath("html/body/div[1]/form/div/button").submit()
        time.sleep(3)
    def clickevent(self,type,value):
        if type=="id":
            dr.find_element_by_id(value).submit()
        elif type=="name":
            dr.find_element_by_name(value).submit()
        elif type=="xpath":
            dr.find_element_by_xpath(value).submit()
        elif type=="link_text":
            dr.find_element_by_link_text(value).submit()
    def gettext(self,type,value):
        if type=="id":
            t=dr.find_element_by_id(value).text
        elif type=="name":
            t=dr.find_element_by_name(value).text
        elif type=="xpath":
            t=dr.find_element_by_xpath(value).text
        elif type=="link_text":
            t=dr.find_element_by_link_text(value).text
        return t
    def sendkeys(self,type,value,value1):
        if type=="id":
            dr.find_element_by_id(value).send_keys(value1)
        elif type=="name":
            t=dr.find_element_by_name(value).send_keys(value1)
        elif type=="xpath":
            t=dr.find_element_by_xpath(value).send_keys(value1)
        elif type=="link_text":
            t=dr.find_element_by_link_text(value).send_keys(value1)
