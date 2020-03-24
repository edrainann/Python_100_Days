# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 
# @Author  : Edrain
import pytest


@pytest.mark.parametrize("n", [1])
def test_feb(n):
    """递归函数
       输出斐波那契数列"""
    if n <= 1:
        return 1
    else:
        return test_feb(n - 1) + test_feb(n - 2)


@pytest.mark.parametrize('passwd', ['123456', 'aa', 'bb'])
def test_passwd_length(passwd):
    assert len(passwd) >= 8

#
# if __name__ == "__main__":
#     pytest.main(["-s", "test_fibonacci_01.py"])
