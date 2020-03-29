from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class App01Config(AppConfig):
    name = 'app01'

    def ready(self):
        autodiscover_modules('pritice')


"""

在每个项目应用中的apps.py文件中的 App01Config类下定义ready(self)方法后，
在项目启动后，就会去已经注册的所有app的目录下找要导入的文件，并自动导入。

在项目启动后代码autodiscover_modules('pritice')导入的文件会执行两次，是因为在运行项目时django会开启两个线程，一个执行项目
另外一个是检查项目中有没有变动，有变动后就重新加载项目，如果不想重载项目就运行：
     python manage.py runserver 120.0.0.1:8001 --noreload
也可以在pycharm中可以设置

注意：
    如果xxxx.py执行的代码向 “某个神奇的地方” 放入了一些值。之后的路由加载时，可以去“某个神奇的地方”读取到原来设置的值。

"""
