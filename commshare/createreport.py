import unittest
import HTMLTestRunner
class htmltestrunner():
    def htmltest(self,filename,ftitle,fdescription,runsuit):
        filepath="../report/"+filename
        with open(filepath,"wb") as fhtml:
            HTMLTestRunner.HTMLTestRunner(
                stream=fhtml,
                title=ftitle,
                verbosity=2,
                description=fdescription).run(runsuit)
