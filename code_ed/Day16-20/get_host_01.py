#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5
# @Author  : Edrain
import os
from pathlib import Path

from dotenv import load_dotenv


def get_conf(func):
    def wrapper(*args):
        load_dotenv()
        env_path = Path('.') / '19.env'
        load_dotenv(dotenv_path=env_path)
        result = func(*args)
        return result
    return wrapper


@get_conf
def dis_conf(sb):
    print("------")
    DB_URL = os.getenv(sb)
    return DB_URL


read = dis_conf("sc_pre_loan_host")
print(read, '--abc')


