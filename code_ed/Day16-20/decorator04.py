# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 
# @Author  : Edrain
"""日志级别打印"""
import logging


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warning("%s is running" % func.__name__)
                print('-------')
            elif level == "info":
                logging.info("%s is running" % func.__name__)
                print("====")
            return func(*args)

        return wrapper

    return decorator


@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)


if __name__ == '__main__':
    foo()
