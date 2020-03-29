from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
from authView import models
from utils.auth import MyAuth
from utils.permission import MyPermission
from utils.throttl import MyThrottle


class AuthDemo(APIView):

    def get(self, request):

        return Response('认证组件')


class Login(APIView):

    def post(self, request):

        username  = request.data.get('username')
        pwd = request.data.get('pwd')
        token = uuid.uuid4()
        type = request.data.get('type')
        models.User.objects.create(username=username, password=pwd, type=type, token=token)

        return Response('创建用户成功')
    

class TestVier(APIView):
    
    authentication_classes = [MyAuth, ]
    permission_classes = [MyPermission, ]
    throttle_classes = [MyThrottle, ]

    def get(self, request):

        print(request.user)
        print(request.auth)
        print(request.META)

        return Response('认证测试')

a = {
    'ALLUSERSPROFILE':'C:\ProgramData',
    'APPDATA':'C:\Users\夏天\AppData\Roaming',
    'CLASSPATH':'.;D:\MyDownloads\java\lib\dt.jar;D:\MyDownloads\java\lib\tools.jar',
    'COMMONPROGRAMFILES':'C:\Program Files\Common Files',
    'COMMONPROGRAMFILES(X86)':'C:\Program Files (x86)\Common Files',
    'COMMONPROGRAMW6432':'C:\Program Files\Common Files',
    'COMPUTERNAME':'LAPTOP-SEDRE8NN',
    'COMSPEC':'C:\WINDOWS\system32\cmd.exe',
    'DJANGO_SETTINGS_MODULE':'DRF.settings',
    'DRIVERDATA':'C:\Windows\System32\Drivers\DriverData',
    'HOMEDRIVE':'C:',
    'HOMEPATH':'\Users\夏天',
    'JAVA_HOME':'D:\MyDownloads\java',
    'LOCALAPPDATA':'C:\Users\夏天\AppData\Local',
    'LOGONSERVER':'\LAPTOP-SEDRE8NN',
    'NUMBER_OF_PROCESSORS':'12',
    'ONEDRIVE':'C:\Users\夏天\OneDrive',
    'ONEDRIVECONSUMER':'C:\Users\夏天\OneDrive',
    'OS':'Windows_NT',
    'PATH':r'D:\practice_Python_code\untitled\work_Review\DRF\venv\Scripts;C:\ProgramData\Oracle\Java\javapath;C:\Python37;C:\redis;C:\\Python37\\Scripts;C:\\Program Files\\nodejs;D:\\mysql56\\bin;C:\\Windows\\System32;"D:\\MyDownloads\\java\\bin;D:\\MyDownloads\\java\\jre\\bin";D:\\MyDrivers\\Git\\Git\\cmd;C:\\Users\\澶忓ぉ\\.ssh;C:\\Program Files\\nodejs;C:\\Users\\澶忓ぉ\\AppData\\Local\\Microsoft\\WindowsApps;D:\\study Python\\software install\\pycharm-professional-2018.3.1\\PyCharm 2018.3.1\\bin;d:\\VS Code\\bin;C:\\Users\\澶忓ぉ\\AppData\\Roaming\\npm;C:\\redis;C:\\Python37;C:\\Python37\\Scripts;C:\\Program Files\\nodejs;D:\\mysql56\\bin;C:\\Windows\\System32;"D:\\MyDownloads\\java\\bin;D:\\MyDownloads\\java\\jre\\bin";C:\\Users\\澶忓ぉ\.ssh;D:\MyDrivers\Fiddler;D:\MyDrivers\Anaconda\Scripts;D:\MyDrivers\texlive\texlive\bin\win32;C:\Python37\lib\site-packages\pywin32_system32;C:\Python37\lib\site-packages\pywin32_system32',
    'PATHEXT':'.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW',
    'PROCESSOR_ARCHITECTURE':'AMD64',
    'PROCESSOR_IDENTIFIER':['Intel64 Family 6 Model 158 Stepping 10','GenuineIntel', {'PROCESSOR_LEVEL':'6'}],
    'PROCESSOR_REVISION':'9e0a',
    'PROGRAMDATA':'C:\\ProgramData',
    'PROGRAMFILES':'C:\\Program Files',
    'PROGRAMFILES(X86)':'C:\\Program Files (x86)',
    'PROGRAMW6432':'C:\\Program Files',
    'PROMPT':'(venv) $P$G',
    'PSMODULEPATH':'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules',
    'PUBLIC':'C:\\Users\\Public',
    'PYCHARM':'D:\\study Python\\software install\\pycharm-professional-2018.3.1\\PyCharm 2018.3.1\\bin;',
    'PYCHARM_DISPLAY_PORT':'52103',
    'PYCHARM_HOSTED':'1',
    'PYTHONIOENCODING':'UTF-8',
    'PYTHONPATH':'D:\\practice_Python_code\\untitled\\work_Review\\DRF;D:\\Program Files\\JetBrains\\PyCharm 2019.1.1\\helpers\\pycharm_matplotlib_backend;D:\\Program Files\\JetBrains\\PyCharm 2019.1.1\\helpers\\pycharm_display',
    'PYTHONUNBUFFERED':'1',
    'SESSIONNAME':'Console',
    'SYSTEMDRIVE':'C:',
    'SYSTEMROOT':'C:\\WINDOWS',
    'TEMP':'C:\\Users\\夏天\\AppData\\Local\\Temp',
    'TMP':'C:\\Users\\夏天\\AppData\\Local\\Temp',
    'USERDOMAIN':'LAPTOP-SEDRE8NN',
    'USERDOMAIN_ROAMINGPROFILE':'LAPTOP-SEDRE8NN',
    'USERNAME':'summer',
    'USERPROFILE':'C:\\Users\\夏天',
    'VIRTUAL_ENV':'D:\\practice_Python_code\\untitled\\work_Review\\DRF\\venv',
    'WINDIR':'C:\\WINDOWS',
    '_OLD_VIRTUAL_PATH':'C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Python37;C:\\redis;C:\\Python37\\Scripts;C:\\Program Files\\nodejs;D:\\mysql56\\bin;C:\\Windows\\System32;"D:\\MyDownloads\\java\\bin;D:\\MyDownloads\\java\\jre\\bin";D:\\MyDrivers\\Git\\Git\\cmd;C:\\Users\\澶忓ぉ\\.ssh;C:\\Program Files\\nodejs;C:\\Users\\澶忓ぉ\\AppData\\Local\\Microsoft\\WindowsApps;D:\\study Python\\software install\\pycharm-professional-2018.3.1\\PyCharm 2018.3.1\\bin;d:\\VS Code\\bin;C:\\Users\\澶忓ぉ\\AppData\\Roaming\\npm;C:\\redis;C:\\Python37;C:\\Python37\\Scripts;C:\\Program Files\\nodejs;D:\\mysql56\\bin;C:\\Windows\\System32;"D:\\MyDownloads\\java\\bin;D:\\MyDownloads\\java\\jre\\bin";C:\\Users\\澶忓ぉ\\.ssh;D:\\MyDrivers\\Fiddler;D:\\MyDrivers\\Anaconda\\Scripts;D:\\MyDrivers\\texlive\\texlive\\bin\\win32',
    '_OLD_VIRTUAL_PROMPT':'$P$G',
    'RUN_MAIN':'true',
    'SERVER_NAME':'LAPTOP-SEDRE8NN',
    'GATEWAY_INTERFACE':'CGI/1.1',
    'SERVER_PORT':'8000',
    'REMOTE_HOST':'',
    'CONTENT_LENGTH':'',
    'SCRIPT_NAME':'',
    'SERVER_PROTOCOL':'HTTP/1.1',
    'SERVER_SOFTWARE':'WSGIServer/0.2',
    'REQUEST_METHOD':'GET',
    'PATH_INFO':'/auth/test',
    'QUERY_STRING':'token=45ae1bdf9ad9497baeda599b4df9d947',
    'REMOTE_ADDR':'127.0.0.1',
    'CONTENT_TYPE':'text/plain',
    'HTTP_HOST':'127.0.0.1:8000',
    'HTTP_CONNECTION':'keep-alive',
    'HTTP_CACHE_CONTROL':'max-age=0',
    'HTTP_UPGRADE_INSECURE_REQUESTS':'1',
    'HTTP_USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/79.0.3945.130 Safari/537.36', 'HTTP_SEC_FETCH_USER':'?1',
    'HTTP_ACCEPT':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'HTTP_SEC_FETCH_SITE':'none',
    'HTTP_SEC_FETCH_MODE':'navigate',
    'HTTP_ACCEPT_ENCODING':['gzip,deflate, br', {'HTTP_ACCEPT_LANGUAGE':'zh-CN,zh;q=0.9', 'HTTP_COOKIE':'csrftoken=2Yob4Szm6u3Vj33IM9AKE5ZD0YNP4NJjwAyfpiLleEBmhS4sjfVHJkdzbMQ54eWv'}],
    'wsgi.input':"<django.core.handlers.wsgi.LimitedStream object at 0x000001ECDB059160>",
    'wsgi.errors':"<_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>",
    'wsgi.version':[(1,0), {'wsgi.run_once':False}],
    'wsgi.url_scheme': 'http',
    'wsgi.multithread':True,
    'wsgi.multiprocess':False,
    'wsgi.file_wrapper':"<class 'wsgiref.util.FileWrapper'>",
    'CSRF_COOKIE':'2Yob4Szm6u3Vj33IM9AKE5ZD0YNP4NJjwAyfpiLleEBmhS4sjfVHJkdzbMQ54eWv'
}

    
    