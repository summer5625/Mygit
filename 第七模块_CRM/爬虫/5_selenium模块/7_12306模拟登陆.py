# -*- coding: utf-8 -*-
# @Time    : 2019/12/6  17:58
# @Author  : XiaTian
# @File    : 7_12306模拟登陆.py
from selenium import webdriver
import time
from PIL import Image
import requests
from hashlib import md5
from selenium.webdriver import ActionChains


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


# 打开登陆页面
bro = webdriver.Chrome(executable_path='chromedriver.exe')
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(1)

time.sleep(1)
login_btn = bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
login_btn.click()

time.sleep(1)
# 将当前打开页面进行截图保存
bro.save_screenshot('aa.png')

# 确定验证码所在区域对应的左上角和右下角的坐标
code_img_ele = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
location = code_img_ele.location  # 确定验证码图片左上角的坐标
size = code_img_ele.size   # 确定验证码图片的大小

# 得到验证码图片对应的左上角和右下角的坐标
rangel = (
    int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))

# 保存验证码图片
i = Image.open('aa.png')
code_img_name = 'code.png'

# 裁剪验证码图片
frame = i.crop(rangel)
frame.save(code_img_name)

# 将验证码图片提交给超级鹰识别

chaojiying = Chaojiying_Client('458684403', 'xiayun519625', '902641')
im = open('code.png', 'rb').read()
result = chaojiying.PostPic(im, 9004)['pic_str']

# 得到验证码图片每个需要选中的物品的坐标

l_list = []
if '|' in result:

    s_list = result.split('|')

    for i in s_list:
        num = i.split(',')
        l_list.append([num[0], num[1]])
else:

    s_list = result.split(',')
    l_list.append([s_list[0],s_list[1]])

# 使用动作链点击选中物品
for item in l_list:
    x = int(item[0])
    y = int(item[1])
    ActionChains(bro).move_to_element_with_offset(code_img_ele, x, y).click().perform()
    time.sleep(0.5)

# 输入用户名和密码并登陆
username = bro.find_element_by_id('J-userName')
password = bro.find_element_by_id('J-password')

username.send_keys('xiazhen12336')
password.send_keys('xiayun519625')

btn = bro.find_element_by_id('J-login')
btn.click()