#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : Edrain
"""
定义一个类描述数字时钟
"""
from time import sleep


class Clock:

    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        time = f'{self._hour:02d}:{self._minute:02d}:{self._second:02d}'
        # time = '%02d:%02d:%02d' % (self._hour, self._minute, self._second)  # 2是宽度很简单。如果整数不够2列就补上0
        return time


def main():
    clock = Clock(1, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
