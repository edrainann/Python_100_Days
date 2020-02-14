# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 
# @Author  : Edrain
import requests
import logging


class TestRequests(object):
    logging.basicConfig()

    def test_get(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
        logging.info(r)
        logging.info(r.text)
