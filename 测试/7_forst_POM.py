# -*- coding: utf-8 -*-
# @Time    : 2019/12/28  18:52
# @Author  : XiaTian
# @File    : 7_forst_POM.py
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self, bro, base_url, title):
        self.bro = bro
        self.base_url = base_url
        self.title = title

    def _open(self, url):
        self.bro.get(url)
        WebDriverWait(self.bro, 10).until(EC.title_is(self.title))

    def open(self):
        self._open(self.base_url)

    def find_element(self, *args):
        WebDriverWait(self.bro, 15).until(EC.visibility_of_element_located(args))
        return self.bro.find_element(*args)


# if __name__ == '__main__':
#
#     bro = webdriver.Chrome('./chromedriver.exe')
#     bro.maximize_window()
#     page = BasePage(bro, 'http://www.baidu.com/', '百度一下，你就知道')
#     page.open()
#     bro.quit()


class LoinPage(BasePage):

    username_loc = (By.ID, 'loginname')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.XPATH, '//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
    message = (By.XPATH, '//div[@class="content layer_mini_info"]/p/span[2]')

    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click() # 为啥参数要加*号，咱也不知道

    def get_message(self):
        return self.find_element(*self.message).text


if __name__ == '__main__':

    base_url = 'https://weibo.com/'
    title = '微博-随时随地发现新鲜事'
    username = 'hahha'
    password = 'hehe'

    bro = webdriver.Chrome('./chromedriver.exe')
    bro.maximize_window()
    login = LoinPage(bro, base_url, title)
    login.open()
    login.type_username(username)
    login.type_password(password)
    login.submit()
    print(login.get_message())











