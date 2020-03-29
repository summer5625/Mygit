# -*- coding: utf-8 -*-
# @Time    : 2019/12/29  1:27
# @Author  : XiaTian
# @File    : browswe_engine.py
import configparser
import os
from selenium import webdriver
from .logger import Logger


logger = Logger(logger='BrowserEngine').getlog()


class BrowserEngine(object):

    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    chrome_path = dir + '/tools/chromedriver.exe'

    def __init__(self, bro):
        self.bro = bro

    def open_browser(self, bro):
        config = configparser.ConfigParser()
        file_path = self.dir + '/config/config.ini'
        config.read(file_path)

        browser = config.get('browserType', 'browserName')
        logger.info('You had select %s browser.' % browser)
        url = config.get('testServer', 'URL')
        logger.info('The test server url is: %s' % url)

        if browser == 'Chrome':
            bro = webdriver.Chrome(self.chrome_path)
            logger.info('Starting Chrome browser.')
        elif browser == 'IE':
            bro = webdriver.Ie()
            logger.info('Starting IE browser.')
        elif browser == 'Firefox':
            bro = webdriver.Firefox()
            logger.info('Starting firefox browser.')

        bro.get(url)
        logger.info('Open url: %s' % url)
        bro.maximize_window()
        bro.implicitly_wait(10)
        logger.info('Set implicitly wait 10 seconds.')
        return bro

    def quit_browser(self):
        logger.info('Now, Close and quit the browser.')
        self.bro.quit()













