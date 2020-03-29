# -*- coding: utf-8 -*-
# @Time    : 2019/9/24  16:57
# @Author  : XiaTian
# @File    : 3、wsgiref模块.py

from wsgiref.simple_server import make_server


def application(environ,start_response):
    '''
    :param environ: 按照http协议解析数据
    :param start_response: 按照http协议组装数据
    :return:
    '''

    print(type(environ))
    print(environ)

    #获取当前请求的路径
    path = environ.get('PATH_INFO')
    start_response('200 OK', [])
    print(path)
    if path == '/practice':
        with open('login.html','rb') as f:
            data = f.read()

    elif path == '/comment':
        with open('1、vue起步.html','rb') as f:
            data = f.read()

    elif path == '/favicon.ico': #在发请求是会默认每次都发送favicon.ico的地址请求，该请求是一个网址的图标地址，像京东每次访问时都会在页面上显示图标
        with open('favicon.png', 'rb') as f:
            data = f.read()

    return [data]

    # start_response('200 OK', [])  # 两个参数分别是响应首行和响应头，响应头可以为空列表
    # return [b'<h1>hello my love!</h1>'] #返回值必须是列表


#封装socket套接字,里面三个参数分别是 IP，端口和回调函数即自己写的请求处理部分的代码
httped = make_server('127.0.0.1',8090,application)


#等待用户连接
httped.serve_forever()


'''
{'ALLUSERSPROFILE': 'C:\\ProgramData', 
'APPDATA': 'C:\\Users\\夏天\\AppData\\Roaming',
 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 
 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
  'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 
  'COMPUTERNAME': 'LAPTOP-SEDRE8NN', 
  'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe',
   'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData',
    'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 
    'FPS_BROWSER_USER_PROFILE_STRING': 'Default',
     'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\夏天', 
     'LOCALAPPDATA': 'C:\\Users\\夏天\\AppData\\Local', 
     'LOGONSERVER': '\\\\LAPTOP-SEDRE8NN', 
     'NUMBER_OF_PROCESSORS': '12',
      'ONEDRIVE': 'C:\\Users\\夏天\\OneDrive', 
      'ONEDRIVECONSUMER': 'C:\\Users\\夏天\\OneDrive',
       'OS': 'Windows_NT', 
       'PATH': 'C:\\Python37\\Scripts\\;C:\\Python37\\;C:\\Python27\\;C:\\Python27\\Scripts;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;D:\\mysql56\\bin;C:\\Users\\夏天\\AppData\\Local\\Microsoft\\WindowsApps;;D:\\study Python\\software install\\pycharm-professional-2018.3.1\\PyCharm 2018.3.1\\bin;;d:\\VS Code\\bin;C:\\Python37\\lib\\site-packages\\pywin32_system32', 
       'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW', 
       'PROCESSOR_ARCHITECTURE': 'AMD64', '
       PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 10,GenuineIntel',
        'PROCESSOR_LEVEL': '6', 
        'PROCESSOR_REVISION': '9e0a',
         'PROGRAMDATA': 'C:\\ProgramData',
          'PROGRAMFILES': 'C:\\Program Files',
           'PROGRAMFILES(X86)': 'C:\\Program Files (x86)',
            'PROGRAMW6432': 'C:\\Program Files', 
            'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 
            'PUBLIC': 'C:\\Users\\Public',
             'PYCHARM': 'D:\\study Python\\software install\\pycharm-professional-2018.3.1\\PyCharm 2018.3.1\\bin;', 
             'PYCHARM_DISPLAY_PORT': '64806', 
             'PYCHARM_HOSTED': '1', 
             'PYTHONIOENCODING': 'UTF-8',
              'PYTHONPATH': 'D:\\practice_Python_code\\untitled;D:\\Program Files\\JetBrains\\PyCharm 2019.1.1\\helpers\\pycharm_matplotlib_backend;D:\\Program Files\\JetBrains\\PyCharm 2019.1.1\\helpers\\pycharm_display', 
              'PYTHONUNBUFFERED': '1', 
              'SESSIONNAME': 'Console', 
              'SYSTEMDRIVE': 'C:', 
              'SYSTEMROOT': 'C:\\WINDOWS',
               'TEMP': 'C:\\Users\\夏天\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\夏天\\AppData\\Local\\Temp',
                'USERDOMAIN': 'LAPTOP-SEDRE8NN', 
                'USERDOMAIN_ROAMINGPROFILE': 'LAPTOP-SEDRE8NN',
                 'USERNAME': '夏天', 
                 'USERPROFILE': 'C:\\Users\\夏天', 
                 'WINDIR': 'C:\\WINDOWS', 
                 'SERVER_NAME': 'LAPTOP-SEDRE8NN', 
                 'GATEWAY_INTERFACE': 'CGI/1.1',
                  'SERVER_PORT': '8090', 
                  'REMOTE_HOST': '', 
                  'CONTENT_LENGTH': '', 
                  'SCRIPT_NAME': '', 
                  'SERVER_PROTOCOL': 'HTTP/1.1', 
                  'SERVER_SOFTWARE': 'WSGIServer/0.2', 
                  'REQUEST_METHOD': 'GET', 
                  'PATH_INFO': '/', 'QUERY_STRING': '',
                   'REMOTE_ADDR': '127.0.0.1',
                    'CONTENT_TYPE': 'text/plain', 
                    'HTTP_HOST': '127.0.0.1:8090', 
                    'HTTP_CONNECTION': 'keep-alive', 
                    'HTTP_CACHE_CONTROL': 'max-age=0', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', 'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_SEC_FETCH_USER': '?1', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'HTTP_SEC_FETCH_SITE': 'none', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9', 'wsgi.input': <_io.BufferedReader name=664>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}

'''

