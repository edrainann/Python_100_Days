# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 
# @Author  : Edrain
import re

"""
https://www.liaoxuefeng.com/wiki/1016959663602400/1017639890281664
\d{3}表示匹配3个数字，例如'010'；

\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；

\d{3,8}表示3-8个数字，例如'1234567'。

要做更精确地匹配，可以用[]表示范围，比如：

[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。

^表示行的开头，^\d表示必须以数字开头。

$表示行的结束，\d$表示必须以数字结束。

你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。"""


def re_match01(need_regular_string):
    """match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。"""
    re_condition = r"^\d{3}\-\d{3,9}$"
    if re.match(re_condition, need_regular_string):
        print("匹配")
    else:
        print("不匹配")


def re_split01(need_regular_string):
    """正则表达式切分字符串比用固定的字符更灵活"""
    return need_regular_string.split('-')


def re_split02(need_regular_string):
    re_condition = r"\s+"
    # re_condition = r"[\s]+"
    return re.split(re_condition, need_regular_string)


def re_compile(need_regular_string):
    """
    当我们在Python中使用正则表达式时，re模块内部会干两件事情：
    编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
    用编译后的正则表达式去匹配字符串。
    如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，
    接下来重复使用时就不需要编译这个步骤了，直接匹配：
    """
    re_condition = r"^(\d{3})-(\d{3,9})$"
    re_phone = re.compile(re_condition)
    return re_phone.match(need_regular_string).groups()


if __name__ == "__main__":
    need_regular_string01 = "111-0922333"
    need_regular_string02 = "a b   c"
    re_match01(need_regular_string01)
    print(re_split01(need_regular_string01))
    print(re_split02(need_regular_string02))
    print(re_compile(need_regular_string01))
