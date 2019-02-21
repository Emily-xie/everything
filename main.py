#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
--------------------------------------
    date:   2019/2/21
--------------------------------------
    Change Date: 2019/2/21

"""
import HTMLTestRunner
import os
import time
import unittest

from script.test_frist import Test

__author__ = 'xienian@mobike.com'

if __name__ == "__main__":

    # # ----------------------------------
    # # 执行测试用例方法一
    # # 构造测试集
    # suite = unittest.TestSuite()
    # # suite.addTest(Test("test_case1"))
    # suite.addTest(Test("test_case2"))
    # suite.addTest(Test("test_case3"))
    # suite.addTest(Test("test_case4"))
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # # --------------------------------------
    # # 执行测试用例方法二：discover()
    #
    # case_path = '/Users/mobike/python_exp/script'
    #
    # # 获取所有测试用例
    # discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py')
    # suite = unittest.TestSuite()
    # suite.addTest(discover)
    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # --------------------------------------
    # 执行测试用例方法三并生成测试报告

    # 当前文件路口
    curren_path = os.getcwd()
    report_path = os.path.join(curren_path, 'report')
    report = os.path.join(report_path, "report.html")
    # 打开文件，把结果写进文件中，w，如果有内容的话，清空再写
    fp = open(report, 'wb')

    case_path = os.path.join(curren_path, 'script')
    # 获取所有测试用例
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py')
    # 执行测试用例
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况')
    runner.run(discover)
    # 关闭刚才打开的文件
    fp.close()




