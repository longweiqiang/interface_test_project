#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 17:34
# @Author  : Weiqiang.long
# @Site    : 
# @File    : excelVariable.py
# @Software: PyCharm

from util.readConfig import *


class ExcelVariable:
    _CaseId = 0
    _CaseName = 1
    _Comment = 2
    _Path = 3
    _Method = 4
    _Params = 5
    _Data = 6
    _Assert = 7

    def get_case_id(self):
        """
        获取caseid
        :return:
        """
        return ExcelVariable._CaseId

    def get_case_name(self):
        return ExcelVariable._CaseName

    def get_comment(self):
        return ExcelVariable._Comment

    def get_path(self):
        return ExcelVariable._Path

    def get_method(self):
        return ExcelVariable._Method

    def get_params(self):
        return ExcelVariable._Params

    def get_data(self):
        return ExcelVariable._Data

    def get_assert(self):
        return ExcelVariable._Assert

class ExcelData:
    def __init__(self):
        self.opera_excel = OperationExcel()
        self.opera_json = OperationJson()
        self.row = ExcelVariable()

    def get_case_id(self, row):
        """获取用例id"""
        id = self.opera_excel.get_row_cel(row, self.row.get_case_id())
        # float处理
        if type(id) == float:
            id = int(id)
        else:
            id = id
        return id

    def get_case_name(self, row):
        """获取用例名称"""
        return self.opera_excel.get_row_cel(row, self.row.get_case_name())

    def get_comment(self, row):
        """获取用例描述"""
        return self.opera_excel.get_row_cel(row, self.row.get_comment())

    def get_path(self, row):
        """获取接口路径"""
        return self.opera_excel.get_row_cel(row, self.row.get_path())

    def get_method(self, row):
        """获取接口请求方式"""
        return self.opera_excel.get_row_cel(row, self.row.get_method())

    def get_params(self, row):
        """获取接口拼接参数"""
        return self.opera_excel.get_row_cel(row, self.row.get_params())

    def get_data(self, row):
        """获取接口body参数"""
        return self.opera_excel.get_row_cel(row, self.row.get_data())

    # def get_case_data(self, row):
    #     # 获取拼接参数或body参数
    #     params = self.opera_excel.get_row_cel(row, self.row.get_params())
    #     data = self.opera_excel.get_row_cel(row, self.row.get_data())
    #     # 如果拼接参数为小数时，转整型
    #     if type(params) == float:
    #         params = int(params)
    #     # 如果body参数为小数时，转整型
    #     if type(data) == float:
    #         data = int(data)
    #     # 如果拼接参数为空，证明拼接参数无数据，返回body参数
    #     if params == '':
    #         return data
    #     else:
    #         return params
    
    def get_case_data(self, row):
        # 获取拼接参数或body参数
        params = self.opera_excel.get_row_cel(row, self.row.get_params())
        data = self.opera_excel.get_row_cel(row, self.row.get_data())
        if params == '':
            try:
                return self.opera_json.get_json_data(data)
            except KeyError:
                return "Json文件中该key值不存在数据"
        else:
            try:
                return self.opera_json.get_json_data(params)
            except KeyError:
                return "Json文件中该key值不存在数据"

    def get_assert(self, row):
        """获取接口断言数据"""
        return self.opera_excel.get_row_cel(row, self.row.get_assert())



a = ExcelData()
print(a.get_case_data(1))
