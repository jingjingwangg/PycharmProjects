#coding=utf-8
import unittest
from commshare.createreport import htmltestrunner
c=htmltestrunner()
class groupsuit(unittest.TestCase):
    def testgroup(self):
        from commshare import login
        from commshare import loginread
        caselist=("Browser","logintest")
        groupsuit=unittest.TestSuite()
        groupsuit.addTest(unittest.makeSuite(loginread.logintest))
        groupsuit.addTest(unittest.makeSuite(login.Browser))
        #unittest.TextTestRunner(verbosity=2).run(groupsuit)
        c.htmltest("report.html",u"测试用例",u"测试用例",groupsuit)
if __name__ == "__main__":
        unittest.main()
