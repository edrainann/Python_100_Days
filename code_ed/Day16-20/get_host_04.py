#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5
# @Author  : Edrain
import os
from pathlib import Path

from dotenv import load_dotenv


class GetConf:
    def __init__(self, sb):
        self.sb = sb

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            load_dotenv()
            env_path = Path('.') / '19.env'
            load_dotenv(dotenv_path=env_path)
            print(os.getenv(self.sb))
            return func(*args, **kwargs)

        return wrapper


@GetConf("sc_pre_loan_host")
def dis_conf():
    print("------")

#
# read = dis_conf()
# print(read)


@GetConf("sc_pre_loan_host")
class ReadDemo01(object):
    def borrower_auth_sms_code(self):
        path = "/sc/borrower/auth/!/smscode/get"
        url =  path
        print("url:", url)

if __name__ == '__main__':
    rd = ReadDemo01()
    rd.borrower_auth_sms_code()