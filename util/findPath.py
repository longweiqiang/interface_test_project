#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 16:45
# @Author  : Weiqiang.long
# @Site    : 
# @File    : findPath.py
# @Software: PyCharm


import os

def data_dir(fileName,pathName='testFile'):
    """
    查找文件绝对路径
    :param fileName:文件名称
    :param pathName:目录名称
    :return:对应文件的绝对路径
    """
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),pathName,fileName)


# print(data_dir('config','config.ini'))


