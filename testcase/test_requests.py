# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 
# @Author  : Edrain
import json

import requests
import logging


class TestRequests(object):
    logging.basicConfig(level=logging.INFO)

    def test_get(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
        logging.info(r)
        logging.info(r.text)
        logging.info(r.json())
        logging.info(json.dumps(r.json(), indent=2))  # 把对象dumps成字符串
