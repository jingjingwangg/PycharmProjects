from commshare.loginshare import openweb
import unittest,time
p=openweb()
class Browser(unittest.TestCase):
    def setUp(self):
        p.openweb("http://b.anfubaoxian.cn")
    def tearDown(self):
        p.close()
    def test001(self):
        p.login001("","Afb123")
        t1=p.gettext("xpath","html/body/div[1]/form/div/button")
        self.assertEqual(u"登录",t1)
    def test002(self):
        p.login001("admin","Afb12")
        t1=p.gettext("xpath","html/body/div[1]/form/div/button")
        self.assertEqual(u"登录",t1)
    def test003(self):
        p.login001("admin","")
        t1=p.gettext("xpath","html/body/div[1]/form/div/button")
        self.assertEqual(u"登录",t1)
    def test004(self):
        p.login001("admin1","Afb123")
        t1=p.gettext("xpath","html/body/div[1]/form/div/button")
        self.assertEqual(u"登录",t1)
    def test005(self):
        p.login001("admin","Afb123")
        t1=p.gettext("xpath",".//*[@id='adminContent']/header/div[2]/ul/li[7]/a/span")
        self.assertEqual(u"管理员",t1)
if __name__=="__main__":
    unittest.main()