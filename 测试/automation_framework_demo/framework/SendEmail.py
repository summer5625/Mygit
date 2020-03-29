# -*- coding: utf-8 -*-
# @Time    : 2019/12/30  1:29
# @Author  : XiaTian
# @File    : SendEmail.py
import os, sys
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


report_path = os.path.dirname(os.getcwd()) + '/test_report/'


class SendEmail(object):

    def get_report(self):

        dirs = os.listdir(report_path)
        dirs.sort()
        new_report_name = dirs[-1]
        return new_report_name

    def take_messages(self):
        new_report = self.get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = 'BBA JIT自动化测试报告'
        self.msg['data'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(report_path, new_report), 'r', encoding='utf-8') as f:
            mailbody = f.read()

        html = MIMEText(mailbody, _subtype='html', _charset='utf-8') # 测试报告放在正文中
        self.msg.attach(html) # 测试报告附加在msg中

        # 报告以附件形式发送
        att1 = MIMEText(mailbody, 'base64', 'utf-8')
        att1['Content-Type'] = 'application/octet-stream'
        att1['Content-Disposition'] = "attachment; filename='TestReport.html'" # filename是附件的名称

        self.msg.attach(att1)

    def send(self):

        recipients = ['1809650813@qq.com'] # 收件人地址列表
        self.take_messages()
        self.msg['from'] = '458684403@qq.com' # 发件人地址
        toaddrs = recipients

        smtp = smtplib.SMTP()
        smtp.connect()
        smtp.ehlo()
        smtp.login('458684403@qq.com', 'xiayun5625')
        smtp.close()


if __name__ == '__main__':
    sendMail = SendEmail()
    sendMail.send()






















