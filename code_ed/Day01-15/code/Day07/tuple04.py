#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7
# @Author  : Edrain
import os

from dotenv import load_dotenv

info = ("sc_pre_loan_host", "db_username")
for my_item in info:
    print(my_item)


def read_env_01(*args):
    result = []
    for item in args:
        print("i: ", item)
        env = os.getenv(item)
        result.append(env)
    return result


if __name__ == '__main__':
    print(read_env_01("db_ip"))
    print(read_env_01("db_ip", "db_port"))
