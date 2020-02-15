# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 
# @Author  : Edrain
import json
import requests
import logging
import jsonpath


class TestRequests(object):
    logging.basicConfig(level=logging.INFO)
    url = "https://testerhome.com/api/v3/topics.json?limit=2"

    def test_get(self):
        r = requests.get(self.url)
        # r = requests.get("https://www.baidu.com")  # 返回的内容不是json格式的
        logging.info(r)  # <class 'requests.models.Response'>
        logging.info(r.text)  # <class 'str'>
        logging.info(r.json())  # <class 'dict'>
        logging.info(json.dumps(r.json(), indent=2))  # 把dict对象dumps成字符串,<class 'str'>

    def test_post(self):
        r = requests.post(self.url,
                          # params={"a": 1, "b": "string content"},  # 错误的发送post请求
                          # data={"a": 1, "b": "string content"},
                          json={"a": 1, "b": "string content"},
                          headers={"a": "11", "b": "22"},
                          proxies={"https": "127.0.0.1:8889",
                                   "http": "127.0.0.1:8889"},  # 启动charles走代理
                          verify=False  # 关闭认证TLS证书
                          )
        logging.info(r.url)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))

    def test_cookie(self):
        r = requests.get("http://www.httpbin.org/cookies",
                         cookies={"a": "111", "b": "222"})
        logging.info(r.text)

    def test_quote(self):
        url = "https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?"
        r = requests.post(url,
                          params={"category": "1"},
                          headers={"User-Agent": "Xueqiu Android 11.19"},
                          cookies={"xq_a_token": "5806a70c6bc5d5fb2b00978aeb1895532fffe502", "u": "3446260779"}
                          )
        # logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))
        # assert r.json()["error_code"] == "1"
        assert r.json()["error_code"] == "400016"
        assert r.json()["error_code"] == "1"

    def test_get_json_path(self):
        r = requests.get(self.url)
        logging.info(json.dumps(r.json(), indent=2))
        logging.info(jsonpath.jsonpath(r.json(), "$.topics[0].user.login"))
        logging.info(jsonpath.jsonpath(r.json(), "$.topics[?(@.id==22234)].user"))  # 只取出来其中某一个，相等的值，做匹配
        logging.info(jsonpath.jsonpath(r.json(), "$.topics[?(@.id==22234)].user.name"))  # ['一只咸鱼']
        logging.info(jsonpath.jsonpath(r.json(), "$.topics[?(@.id==22234)].user.name")[0])  # 一只咸鱼
        assert jsonpath.jsonpath(r.json(), "$.topics[?(@.id==22234)].user.name")[0] == "哇哈哈"
