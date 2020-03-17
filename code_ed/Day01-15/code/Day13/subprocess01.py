# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 
# @Author  : Edrain
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
