#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23
# @Author  : Edrain
"""
发送邮件
"""
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    sender = 'abcdefg@136.com'
    receivers = ['wahh@qq.com', 'poiu@126.com']
    message = MIMEText('用Python发送邮件的示例代码。', 'plain', 'utf-8')
    message['From'] = Header('哇哈哈', 'utf-8')
    message['To'] = Header('小明', 'utf-8')
    message['Subject'] = Header('假装可以发出去邮件', 'utf-8')
    smtper = SMTP('smtp.136.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'secretpas')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')


if __name__ == '__main__':
    main()
