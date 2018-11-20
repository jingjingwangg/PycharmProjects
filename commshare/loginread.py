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
        type=m.readtestdata("loginreaddate.xml","userinfo1",0,"type1")
        value=m.readtestdata("loginreaddate.xml","userinfo1",0,"values1")
        excep = m.readtestdata("loginreaddate.xml", "userinfo1",0,"except1")
        p.login001(username,password)
        t=p.gettext(type,value)
        time.sleep(4)
        self.assertEqual(excep,t)
        time.sleep(3)

    def test002(self):
        username = m.readtestdata("loginreaddate.xml", "userinfo1",1,"username2")
        password = m.readtestdata("loginreaddate.xml", "userinfo1",1,"password2")
        type = m.readtestdata("loginreaddate.xml", "userinfo1",1,"type2")
        value = m.readtestdata("loginreaddate.xml", "userinfo1",1,"values2")
        excep = m.readtestdata("loginreaddate.xml", "userinfo1",1,"except2")
        p.login001(username, password)
        t = p.gettext(type, value)
        time.sleep(4)
        self.assertEqual(excep,t)
        time.sleep(3)
    def test003(self):
        username = m.readtestdata("loginreaddate.xml", "userinfo1",2,"username3")
        password = m.readtestdata("loginreaddate.xml", "userinfo1",2,"password3")
        type = m.readtestdata("loginreaddate.xml", "userinfo1",2,"type3")
        value = m.readtestdata("loginreaddate.xml", "userinfo1",2,"values3")
        excep = m.readtestdata("loginreaddate.xml", "userinfo1",2,"except3")
        p.login001(username, password)
        t = p.gettext(type,value)
        time.sleep(4)
        self.assertEqual(excep,t)
        time.sleep(3)
    def test004(self):
        username = m.readtestdata("loginreaddate.xml", "userinfo1",3,"username4")
        password = m.readtestdata("loginreaddate.xml", "userinfo1",3,"password4")
        type = m.readtestdata("loginreaddate.xml", "userinfo1",3,"type4")
        value = m.readtestdata("loginreaddate.xml", "userinfo1",3,"values4")
        excep = m.readtestdata("loginreaddate.xml", "userinfo1",3,"except4")
        p.login001(username, password)
        t = p.gettext(type, value)
        time.sleep(4)
        self.assertEqual(excep,t)
        time.sleep(3)

    def test005(self):
        username = m.readtestdata("loginreaddate.xml", "userinfo1",4,"username5")
        password = m.readtestdata("loginreaddate.xml", "userinfo1",4,"password5")
        type = m.readtestdata("loginreaddate.xml", "userinfo1",4,"type5")
        value = m.readtestdata("loginreaddate.xml", "userinfo1",4,"values5")
        excep = m.readtestdata("loginreaddate.xml", "userinfo1",4,"except5")
        p.login001(username, password)
        t = p.gettext(type, value)
        time.sleep(4)
        self.assertEqual(excep,t)
if __name__=="__main__":
    unittest.main()