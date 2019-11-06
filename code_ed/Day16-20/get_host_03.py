#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5
# @Author  : Edrain
import os
from pathlib import Path

from dotenv import load_dotenv


class GetConf:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        load_dotenv()
        env_path = Path('.') / '19.env'
        load_dotenv(dotenv_path=env_path)
        print(os.getenv("sc_pre_loan_host"))
        result = self._func(*args, **kwargs)
        return result


@GetConf
def dis_conf():
    print("------")


read = dis_conf()
print(read)
