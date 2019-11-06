#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5
# @Author  : Edrain
# settings.py
from dotenv import load_dotenv
load_dotenv()

# # OR, the same with increased verbosity
# load_dotenv(verbose=True)
#
# # OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.')/'19.env'
load_dotenv(dotenv_path=env_path)

import os
SECRET_KEY = os.getenv("REDIS_ADDRESS")
DB_URL = os.getenv("sc_pre_loan_host")

print(SECRET_KEY)
print(DB_URL)