# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 
# @Author  : Edrain
"""
读写二进制文件
知道了如何读写文本文件要读写二进制文件也就很简单了，下面的代码实现了复制图片文件的功能。
"""
def main():
    try:
        with open('test.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('test_ao.jpg', 'wb') as fs2:  # 将test.jpg 复制给 test_ao.jpg，若没有test_ao也会创建
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


if __name__ == '__main__':
    main()