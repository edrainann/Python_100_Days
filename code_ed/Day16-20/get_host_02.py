#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5
# @Author  : Edrain
import os
from pathlib import Path

from dotenv import load_dotenv

def get_conf(sb):
    def deco(func):
        def wrapper(*args):
            load_dotenv()
            env_path = Path('.') / '19.env'
            load_dotenv(dotenv_path=env_path)
            print(os.getenv(sb))
            result = func(*args)
            return result
        return wrapper
    return deco

@get_conf("sc_pre_loan_host")
def dis_conf():
    print("------")
    return


read = dis_conf()
print(read, '_abc')


