# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 
# @Author  : Edrain
import logging


class Logging:
    def __init__(self, level):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif self.level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)

        return wrapper


@Logging(level="warn")
def add(x, y=10):
    return x + y

print(add(5))