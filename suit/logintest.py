#封装测试套
#coding:utf-8
import unittest
class logintest(unittest.TestCase):
    def testlogin(self):
        from commshare.login import Browser
        caselist=("test001","test002","test003","test004","test005")
        suit=unittest.TestSuite() #声明测试套
        for tmp in caselist:
            suit.addTest(Browser(tmp))
        unittest.TextTestRunner(verbosity=2).run(suit)
if __name__=="__main__":
    unittest.main()