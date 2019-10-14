#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30
# @Author  : Edrain
"""
百分制成绩转换为等级制成绩
"""
# v1
# score = float(input("请输入百分制成绩："))
# if score >= 90:
#     print("A")
# elif score < 90 and score >=80 :
#     print("B")
# elif score < 80 and score >=70 :
#     print("C")
# elif score < 70 and score >= 60:
#     print("D")
# else:
#     print("E")

# v2
score = float(input("请输入成绩："))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"
print("对应的等级是：", grade)
