#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
--------------------------------------
    date:   2019/2/21
--------------------------------------
    Change Date: 2019/2/21

"""
import logging
import os

__author__ = 'xienian@mobike.com'

curren_path = os.getcwd()
log_path = os.path.join(curren_path, 'report')
FORMAT = '[%(asctime)s] --Log-- %(name)s: %(levelname)s %(message)s' #设置日志输出格式

logging.basicConfig(level=logging.INFO,filename="{log_path}/arc.log".format(log_path = log_path),
                    filemode='w',format=FORMAT)

class Logger:
    def __init__(self):
        pass

    def debug(self, msg):
        logging.debug(msg)

    def info(self, msg):
        logging.info(msg)

    def error(self, msg):
        logging.error(msg)

    def warning(self, msg):
        logging.warning(msg)
