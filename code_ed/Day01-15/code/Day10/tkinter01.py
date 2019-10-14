#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14
# @Author  : Edrain
"""
基本上使用tkinter来开发GUI应用需要以下5个步骤：
导入tkinter模块中我们需要的东西。
创建一个顶层窗口对象并用它来承载整个GUI应用。
在顶层窗口对象上添加GUI组件。
通过代码将这些GUI组件的功能组织起来。
进入主事件循环(main loop)。
Tk为控件的摆放提供了三种布局管理器，通过布局管理器可以对控件进行定位，这三种布局管理器分别是：
Placer（开发者提供控件的大小和摆放位置）、Packer（自动将控件填充到合适的位置）和Grid（基于网格坐标来摆放控件）
"""
import tkinter
import tkinter.messagebox


def main():
    flag = True

    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'hello,world') if flag else ('blue', 'Goodbye,world')
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示的哇', '确定要退出嚒？'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()  # 注意k是小写
    # 设置窗口大小
    top.geometry('240x160')  # x 是小写的 x
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello,world', font='Arial -20', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
