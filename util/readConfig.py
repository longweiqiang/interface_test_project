#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 15:56
# @Author  : Weiqiang.long
# @Site    : 
# @File    : readConfig.py
# @Software: PyCharm
import json
import os
import codecs
import configparser
import xlrd
from xlutils.copy import copy
from util.findPath import *

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.ini')
# configPath = os.path.join(proDir, "config.ini")

class ReadConfigIni:
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


class OperationJson:

    def getJson(self):
        """
        获取json文件内容
        :return: 文件内容
        """
        with open(data_dir('test.json'), encoding='utf-8') as f:
            return json.load(f)

    def get_json_data(self, key):
        """
        通过key值查找对应的value值
        :param key: json文件中key
        :return: key对应的value
        """
        return self.getJson()[key]


class OperationExcel:

    def getExcel(self,fileName='case.xls',sheetIndex=0):
        """
        获取excel文件
        :param fileName: 文件名称
        :param sheetIndex: sheet下标
        :return: sheet内容
        """
        excel_data = xlrd.open_workbook(data_dir(fileName))
        sheet = excel_data.sheet_by_index(sheetIndex)
        return sheet

    def get_rows(self):
        """
        获取excel文件行数
        :return: 行数量
        """
        return self.getExcel().nrows

    def get_row_cel(self, row, col):
        """
        获取单元格内容
        :param row:行
        :param col:列
        :return:对应单元格内容
        """
        return self.getExcel().cell_value(row, col)

    # def get_test_case_data(self,):










# opera = OperationJson()
# print(opera.get_json_data("walmart_c_index_001"))






