#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
--------------------------------------
    date:   2018/12/27
--------------------------------------
    Change Date: 2018/12/27

"""
import json
import re
import unittest

from util.log_util import Logger

__author__ = 'xienian@mobike.com'


def outer(func):
    def inner(*args):
        print("---->>>------")
        func(*args)
    return inner

@outer
def test_sum(x, y):
    print('x+y=', x + y)

class Test(unittest.TestCase):

    def setUp(self):
        # self.number = input("Enter a number:")
        # self.number = int(self.number)
        self.number = 10
        pass

    def test_case1(self):
        print(self.number)
        self.assertEqual(self.number, 10, msg="Your input is not 10")

    def test_case2(self):
        test_sum(1,2)
        dict1 = {"age": "12"}
        json_du = json.dumps(dict1)
        print(json_du)

        # mat = re.search('MBK\d{23}(BF)|MBK\d{17}','MBK86783453001548642312297BF')
        #
        # mata22 = re.search('\d{10}|\d{13}', '1548642236433')
        #
        # mata = re.search('\{\'seconds\': \d{10}(,)+\'nanos\': \d{9}\}', "{'seconds':1550197994}")
        # # print('---00000----',mat)
        #
        # print('---00000----', mata)
        # print(self.number)
        # self.assertEqual(self.number, 20, msg="Your input is not 20")
        Logger().info('log info')

    @unittest.skip("暂时跳过用例3的测试")
    def test_case3(self):
        print(self.number)
        self.assertEqual(self.number, 30, msg="Your input is not 30")

    @unittest.skipIf(3 > 2, "3>2,该用例不用执行")
    def test_case4(self):
        print(self.number)
        self.assertEqual(self.number, 40, msg="Your input is not 40")

    def tearDown(self):
        print("Test over")

