#coding:utf-8
__author__ = 'poptest'
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from commshare.readdatexml import readdata
p=readdata()
class SendEmail():
    def sendemail(self):
        sender = p.readtestdata("send.xml","userinfo",0,"sender1")
        receiver = p.readtestdata("send.xml","userinfo",0,"receiver1")
        subject = p.readtestdata("send.xml","userinfo",0,"subject1")
        smtpserver = p.readtestdata("send.xml","userinfo",0,"smtpserver1")
        username = p.readtestdata("send.xml","userinfo",0,"username1")
        password = p.readtestdata("send.xml","userinfo",0,"password1")
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject
        text_msg = MIMEText("<html><body><p><span style='color: red'>;&nbsp;&nbsp; hi all:</span></p><p>&nbsp;&nbsp;&nbsp;&nbsp;附件为本次回归测试报告，请各位查收!</br></p></body></html>",'html','utf-8')
        msgRoot.attach(text_msg)
        #构造附件
        att = MIMEText(open('../report/report.html', 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="reporter.htm"'
        msgRoot.attach(att)
        smtp = smtplib.SMTP()
        smtp.connect(host=smtpserver,port='25')
        smtp.login(username,password)
        smtp.sendmail(sender,receiver,msgRoot.as_string())
        smtp.quit()
