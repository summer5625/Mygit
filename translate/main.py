# -*- coding: utf-8 -*-
# @Time    : 2020/3/9  17:19
# @Author  : XiaTian
# @File    : main.py
import xlrd
import os
import time
from BaiduTransAPI import translate
import xlwt
from xlutils.copy import copy


LANGUAGE_POOL = {
    'zh': '中文',
    'en': '英语',
    'yue': '粤语',
    'wyw': '文言文',
    'jp': '日语',
    'kor': '韩语',
    'fra': '法语',
    'spa': '西班牙语',
    'th': '泰语',
    'ara': '阿拉伯语',
    'ru': '俄语',
    'pt': '葡萄牙语',
    'de': '德语',
    'it': '意大利语',
    'el': '希腊语',
    'nl': '荷兰语',
    'pl': '波兰语',
    'bul': '保加利亚语',
    'est': '爱沙尼亚语',
    'dan': '丹麦语',
    'fin': '芬兰语',
    'cs': '捷克语',
    'rom': '罗马尼亚语',
    'sol': '斯洛文尼亚语',
    'swe': '瑞典语',
    'hu': '匈牙利语',
    'cht': '繁体中文',
    'vie': '越南语'
}

ERROR_CODE = {
    '52000': '成功',
    '52001': '请求超时',
    '52002': '系统错误',
    '52003': '未授权用户',
    '54000': '必填参数为空',
    '54001': '签名错误',
    '54003': '访问频率受限',
    '54004': '账户余额不足',
    '54005': '长query请求频繁，3S后再试',
    '58000': '客户端IP非法',
    '58001': '译文语言方向不支持',
    '58002': '服务当前已关闭，请前往管理控制台开启',
    '90107': '认证未通过或未生效，请前往查看认证进度'
}


class Translate:


    def __init__(self, fromLang='auto', toLang='zh'):
        '''
        :param fromLang: 源语言
        :param toLang: 目标语言
        '''

        self.fromLang = fromLang
        self.toLang = toLang

    def translation(self, content):

        result = translate(self.fromLang, self.toLang, content)
        error_code = result.get('error_code')

        if error_code and str(error_code) != '52000':
            print(ERROR_CODE[error_code])
            return

        data = self.paser(result)
        file_path = self.get_file_path()
        self.save_to_excel(data, file_path)


    def paser(self, result):
        data = []
        row_dict = {}
        row_dict['form'] = LANGUAGE_POOL[result['from']]
        row_dict['to'] = LANGUAGE_POOL[result['to']]
        translated = result['trans_result'][0]
        row_dict['content'] = translated['src']
        row_dict['translated'] = translated['dst']
        data.append(row_dict)

        return data

    def save_to_excel(self, data, file_path):
        try:
            oldbook = xlrd.open_workbook(file_path)
            sheet = oldbook.sheet_by_index(0)
            newbook = copy(oldbook)
            book = newbook.get_sheet(0)
            i = sheet.nrows

            for row in data:
                book.write(i, 0, row['form'])
                book.write(i, 1, row['content'])
                book.write(i, 2, row['to'])
                book.write(i, 3, row['translated'])

                i += 1
            os.remove(file_path)
            newbook.save(file_path)
            print('写入excel成功')
        except Exception:
            print('写入excel失败')

    def get_file_path(self):

        root_path = os.path.dirname(os.path.abspath(__file__))
        now = time.localtime()
        file_name = time.strftime('%Y-%m-%d', now) + '.xls'
        file_path = os.path.join(root_path, 'files', file_name)


        if not os.path.exists(file_path):

            try:
                workbook = xlwt.Workbook(encoding='utf-8')
                sheet = workbook.add_sheet('translate')
                head = ['源语言', '翻译内容', '目标语言', '翻译结果']  # 表头
                for h in range(len(head)):
                    sheet.write(0, h, head[h])

                workbook.save(file_path)
            except Exception:
                print('创建新excel失败')

        return file_path


if __name__ == '__main__':

    t = Translate()
    t.translation('summer')































