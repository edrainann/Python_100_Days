#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22
# @Author  : Edrain
"""例子1：将耗时间的任务放到线程中以获得更好的用户体验。
如下所示的界面中，有“下载”和“关于”两个按钮，用休眠的方式模拟点击“下载”按钮会联网下载文件需要耗费10秒的时间，
如果不使用“多线程”，我们会发现，当点击“下载”按钮后整个程序的其他部分都被这个耗时间的任务阻塞而无法执行了，
这显然是非常糟糕的用户体验，代码如下所示。
"""
import tkinter
import tkinter.messagebox
from time import sleep


def download():
    # 模拟下载任务需要花费10秒钟时间
    sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成')


def show_about():
    tkinter.messagebox.showinfo('关于', '作者：哇哈哈')


def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')  # 按钮 放在 底部
    tkinter.mainloop()  # 启动主窗口的消息循环


if __name__ == '__main__':
    main()
