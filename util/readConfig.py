#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 15:56
# @Author  : Weiqiang.long
# @Site    : 
# @File    : readConfig.py
# @Software: PyCharm

import os
import codecs
import configparser

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.ini')
# configPath = os.path.join(proDir, "config.ini")

class ReadConfig:
    def __init__(self):
        fd = open(CONFIG_FILE)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(CONFIG_FILE, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(CONFIG_FILE)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value