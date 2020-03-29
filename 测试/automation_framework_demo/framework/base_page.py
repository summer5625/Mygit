# -*- coding: utf-8 -*-
# @Time    : 2019/12/29  14:09
# @Author  : XiaTian
# @File    : base_page.py
import time
import os
from selenium.common.exceptions import NoSuchElementException
from .logger import Logger

logger = Logger(logger='BasePage').getlog()


class BasePage(object):

    def __init__(self, bro):
        self.bro = bro

    # 结束测试
    def quit_browser(self):
        self.bro.quit()

    # 浏览器前进
    def forward(self):
        self.bro.forward()
        logger.info('Click forward on current page.')

    # 浏览器后退
    def back(self):
        self.bro.back()
        logger.info('Click back on current page.')

    # 设置等待时间
    def wait(self, seconds):
        self.bro.implicitly_wait(seconds)
        logger.info('wait for %d seconds.' % seconds)

    # 关闭当前窗口
    def close(self):
        try:
            self.bro.close()
            logger.info('Closing and quit the browser.')
        except Exception as e:
            logger.error('Failed to quit the browser with %s' % e)

    # 获取网页截图
    def get_window_img(self):
        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/screenshots/'
        name = time.strftime('%m-%d%H%M%S') + '.png'
        file_name = file_path + name
        try:
            self.bro.get_screenshot_as_file(file_name)
            logger.info('Had take screenshot and save to folder : /screenshots')
        except Exception as e:
            logger.error('Failed to take screenshot! %s' % e)
            self.get_window_img()

    # 页面元素定位
    def find_element(self, selector):

        element = ''

        if '=>' not in selector:
            return self.bro.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        print('se_v-->', selector_value)

        if selector_by == 'i' or selector_by == 'id':
            try:
                element = self.bro.find_element_by_id(selector_value)
                logger.info(
                    "Had find the element '{0}' successful by {1} via value:{2}".format(element.text, selector_by,
                                                                                        selector_value))
            except NoSuchElementException as e:
                logger.error('NoSuchElementException: {0}'.format(e))
                self.get_window_img()
        elif selector_by == 'n' or selector_by == 'name':
            element = self.bro.find_element_by_name(selector_value)
        elif selector_by == 'c' or selector_by == 'class_name':
            element = self.bro.find_element_by_class_name(selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.bro.find_element_by_link_text(selector_value)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = self.bro.find_element_by_partial_link_text(selector_value)
        elif selector_by == 't' or selector_by == 'tag_name':
            element = self.bro.find_element_by_tag_name(selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                element = self.bro.find_element_by_xpath(selector_value)
                logger.info("Had find the element '{0}' successful by {1} via value:{2}".format(element.text, selector_by,
                                                                                        selector_value))
            except Exception as e:
                logger.error('NoSuchElementException: {0}'.format(e))
                self.get_window_img()
        elif selector_by == 's' or selector_by == 'selector_selector':
            element = self.bro.find_element_by_css_selector(selector_value)
        else:
            raise NameError('Please enter a valid type of targeting elements.')
        print('el-->', element)
        return element

    # 输入定位条件
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info('Had type {0} in inputBox'.format(text))
        except NameError as e:
            logger.error('Failed to type in input box with {0}'.format(e))

    # 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info('The element {0} was clicked.'.format(selector))
        except NameError as e:
            logger.error('Failed to click the element with {0}'.format(e))

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info('Clear text in input box before typing.')
        except NameError as e:
            logger.error('Failed to clear in input box with {0}'.format(e))
            self.get_window_img()

    # 网页标题
    def get_page_title(self):
        logger.info('Current page title is {0}'.format(self.bro.title))
        return self.bro.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info('Sleep for {0} seconds'.format(seconds))
















