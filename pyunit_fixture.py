#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# File Name:   ut2.py
# Purpose:    
#
# Author:      Ke Wang
#
# Created:     2019-11-03
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
 
import unittest

class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def setUp(self):
         # 每个测试用例执行之前做操作
         print('\nStarting test ...')

    def tearDown(self):
         # 每个测试用例执行之后做操作
         print('Test ending ...')

    @classmethod
    def setUpClass(self):
    # 必须使用@classmethod 装饰器,所有test运行前运行一次
         print('Init testing one time ...')

    @classmethod
    def tearDownClass(self):
    # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
         print('Run once cleaning up ...')

    def test_a_run(self):
         print("Run test a ...")
         self.assertEqual(1, 1)  # 测试用例

    def test_b_run(self):
         print("Run test b ...")
         self.assertEqual(2, 2)  # 测试用例

if __name__ == '__main__':
     unittest.main(verbosity=1)#运行所有的测试用例
