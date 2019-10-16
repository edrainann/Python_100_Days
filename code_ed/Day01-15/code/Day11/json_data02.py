# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 
# @Author  : Edrain
"""
在Python中要实现序列化和反序列化除了使用json模块之外，还可以使用pickle和shelve模块，
但是这两个模块是使用特有的序列化协议来序列化数据，因此序列化后的数据只能被Python识别。
需要将内存中的变量转化为可存储的对象或者可传输的对象，这样的过程就叫做序列化。
JSON可以理解为序列化的标准格式。
dumps序列化: python --> json
loads反序列化：json --> python
"""
import requests
import json


def main():
    resp = requests.get('https://api.douban.com/v2/movie/imdb/tt0111161?apikey=0df993c66c0c636e29ecbb5344252a4a')
    data_model = json.loads(resp.text)
    print(data_model)
    print(data_model['rating'])
    for movie in data_model['rating']:
        print(movie)


if __name__ == '__main__':
    main()