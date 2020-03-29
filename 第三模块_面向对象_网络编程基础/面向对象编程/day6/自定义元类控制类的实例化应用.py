# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 14:12
# @Author  : XiaTian
# @File    : 自定义元类控制类的实例化应用.py

# 单例模式：将参数都一样的不同对象，将他们的内存空间整合成一个内存空间，即在每个对象生成时，申请的内存空间相同

class MySQL:
    _instance = None

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306

    @classmethod
    def singleton(cls):
        if not cls._instance:
            obj = cls()
            cls._instance = obj
        return cls._instance

    def conn(self):
        pass

    def execte(self):
        pass


obj1 = MySQL.singleton()
obj2 = MySQL.singleton()
obj3 = MySQL.singleton()
print(id(obj1))
print(id(obj2))
print(id(obj3))
print(obj1 is obj2 is obj3)


# 元类方式

class Mymeta(type):  # 定义一个继承type类的元类

    def __init__(self, class_name, class_bases, class_dict):
        if not class_name.istitle():
            raise TypeError('首字母必须大写')

        if not '__doc__' in class_dict or not class_dict['__doc__'].strip():
            raise TypeError('必须有注释，且注释不能为空')
        super(Mymeta, self).__init__(class_name, class_bases, class_dict)
        self._instance = None  # 设置MySQL类的_instance属性

    def __call__(self, *args, **kwargs):
        if not self._instance:  # 判断类里面有没有_instance属性，没有就实例化一个对象
            obj = object.__new__(self)
            self.__init__(obj)
            self._instance = obj
        return self._instance


class Mysql(object, metaclass=Mymeta):
    '''
    MySQL
    '''

    _instance = None

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306

    def conn(self):
        pass

    def execte(self):
        pass


obj1 = Mysql()
obj2 = Mysql()
obj3 = Mysql()

print(obj1 is obj2 is obj3)
