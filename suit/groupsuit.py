#coding:utf-8
import unittest
class groupsuit(unittest.TestCase):
    def testgroup(self):
        from commshare import login
        from commshare import loginread
        caselist=("Browser","logintest")
        groupsuit=unittest.TestSuite()
        groupsuit.addTest(unittest.makeSuite(login.Browser))
        groupsuit.addTest(unittest.makeSuite(loginread.logintest))
        unittest.TextTestRunner(verbosity=2).run(groupsuit)
if __name__=="__main__":
    unittest.main()