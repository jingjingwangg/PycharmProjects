#执行报错
#coding=utf-8
from commshare.openweb import openweb
from commshare.readdatexml import readdata
import time
import unittest
m=readdata()
p=openweb()
class logintest(unittest.TestCase):
    def setUp(self):
        p.openweb("http://b.anfubaoxian.cn")
    def tearDown(self):
        p.close()
    def test001(self):
        username=m.readtestdata("loginreaddate.xml","userinfo1",0,"username1")
        password=m.readtestdata("loginreaddate.xml","userinfo1",0,"password1")
        p.login001(username,password)
        t=p.gettext("xpath","html/body/div[1]/form/div/button")
        time.sleep(4)
        self.assertEqual(u"登录",t)
        time.sleep(3)

    def test002(self):
        username = m.readtestdata("loginreaddate.xml", "userinfo1",1,"username2")
        password = m.readtestdata("loginreaddate.xml", "userinfo1",1,"password2")
        p.login001(username, password)
        t = p.gettext("xpath", "html/body/div[1]/form/div/button")
        time.sleep(4)
        self.assertEqual(u"登录",t)
        time.sleep(3)
    def test003(self):
        username = m.readtestdata("loginreaddate.xml", "userinfo1",2,"username3")
        password = m.readtestdata("loginreaddate.xml", "userinfo1",2,"password3")
        p.login001(username, password)
        t = p.gettext("xpath", "html/body/div[1]/form/div/button")
        time.sleep(4)
        self.assertEqual(u"登录", t)
        time.sleep(3)
    def test004(self):
        username = m.readtestdata("loginreaddate.xml", "userinfo1",3,"username4")
        password = m.readtestdata("loginreaddate.xml", "userinfo1",3,"password4")
        p.login001(username, password)
        t = p.gettext("xpath", "html/body/div[1]/form/div/button")
        time.sleep(4)
        self.assertEqual(u"登录", t)
        time.sleep(3)

    def test005(self):
        username = m.readtestdata("loginreaddate.xml", "userinfo1",4,"username5")
        password = m.readtestdata("loginreaddate.xml", "userinfo1",4,"password5")
        p.login001(username, password)
        t = p.gettext("xpath", ".//*[@id='adminContent']/header/div[2]/ul/li[7]/a/span")
        time.sleep(4)
        self.assertEqual(u"管理员", t)
if __name__=="__main__":
    unittest.main()