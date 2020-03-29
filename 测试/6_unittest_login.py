# -*- coding: utf-8 -*-
# @Time    : 2019/12/28  15:18
# @Author  : XiaTian
# @File    : 6_unittest_login.py
import unittest
from selenium import webdriver
import time


class LoginCase(unittest.TestCase):

    def setUp(self):
        self.bro = webdriver.Chrome('./chromedriver.exe')
        self.bro.maximize_window()

    def login(self, username, password):
        self.bro.get('https://passport.cnblogs.com/user/signin')
        self.bro.find_element_by_id('LoginName').send_keys(username)
        self.bro.find_element_by_id('Password').send_keys(password)
        self.bro.find_element_by_xpath('//*[@id="submitBtn"]/span[1]').click()

    def test_login_success(self): # ppp
        self.login('夏天真热', 'xiayun519625')
        time.sleep(3)
        link = self.bro.find_element_by_id('lnk_current_user')
        self.assertTrue('夏天真热' in link.text)
        self.bro.get_screenshot_as_file('login_success.png')

    def test_login_pwd_error(self): # pp
        self.login('夏天真热', 'xiayun519')
        time.sleep(3)
        error_msg = self.bro.find_element_by_class_name('ajax-error-box').text
        self.assertIn('用户名或密码错误', error_msg)
        self.bro.get_screenshot_as_file('login_pwd_error.png')

    def test_login_pwd_null(self):
        self.login('夏天真热', '')
        time.sleep(3)
        error_msg = self.bro.find_element_by_id('Password-error').text
        self.assertEqual(error_msg, '请输入密码')
        self.bro.get_screenshot_as_file('login_pwd_null.png')

    def test_login_user_error(self): # pp
        self.login('夏天', 'xiayun519625')
        time.sleep(3)
        error_msg = self.bro.find_element_by_id('ajax-error-box').text
        self.assertIn('用户名或密码错误', error_msg)
        self.bro.get_screenshot_as_file('login_user_error.png')

    def test_login_user_null(self):
        self.login('', '!qaz2wsx')  # 用户名为空，密码正确
        error_message = self.bro.find_element_by_id('LoginName-error').text
        self.assertEqual(error_message, '请输入登录用户名')  # 用assertEqual(a,b)方法来断言  a == b
        self.bro.get_screenshot_as_file("login_user_null.jpg")

    def tearDown(self):
        time.sleep(2)
        print('自动测试完毕！')
        self.bro.quit()


if __name__ == '__main__':

    unittest.main()
