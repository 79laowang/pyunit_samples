#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# File Name:   run_testmodule.py.py
# Purpose:    
#
# Author:      Ke Wang
#
# Created:     2019-11-05
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
 
import sys
import unittest
 
import pyunit_testmodule
 
def main():
    suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromModule(pyunit_testmodule)
    ])
     
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        return 0
    else:
        return 1
 
if __name__ == '__main__':
    sys.exit(
        int(main())
    )
