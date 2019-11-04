#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# File Name:   pyunit_testsuite.py
# Purpose:    
#
# Author:      Ke Wang
#
# Created:     2019-11-04
# Copyright:   (c) Ke Wang 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from selenium import webdriver
import unittest
import shutil
import os

class WebTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('Init testing one time ...')  
        print("Check the geckodriver if exists ...")
        cmd = 'geckodriver'
        if shutil.which(cmd) is None:
            print('Install the geckodriver ...')
            import urllib.request
            import tarfile
            url = 'https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz'
            fr = urllib.request.urlopen(url)
            fname = url.split('/')[-1]
            with open(fname,'wb') as fout:
                fout.write(fr.read())
            if os.path.exists(fname): 
                print("Extracting the file %s",fname)
                tar = tarfile.open(fname)
                tar.extractall('/tmp')
                tar.close()
                if os.path.exists('/tmp/%s' % cmd) :
                    sudoCmd = 'cp /tmp/%s /usr/local/bin' % cmd
                    os.system('sudo -s %s' % sudoCmd)

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://github.com/79laowang')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_link1(self):
        self.driver.find_element_by_link_text('Shell_scripts').click()
        url = self.driver.current_url
        self.assertEqual(url, 'https://github.com/79laowang/Shell_scripts')

    def test_link2(self):
        self.driver.find_element_by_link_text('Clang-100-examples').click()
        url = self.driver.current_url
        self.assertEqual(url, 'https://github.com/79laowang/Clang-100-examples')

def main():
    suite = unittest.TestSuite()
    suite.addTest(WebTest('test_link1'))
    suite.addTest(WebTest('test_link2'))
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()
