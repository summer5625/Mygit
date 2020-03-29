# -*- coding: utf-8 -*-
# @Time    : 2019/11/2  16:20
# @Author  : XiaTian
# @File    : app.py

import uitrl

print(uitrl.site) # <uitrl.AdminSite object at 0x0000024901E324E0>


import uitrl

print(uitrl.site) # <uitrl.AdminSite object at 0x0000024901E324E0>


"""

结果来看两次打印结果一样，说明在python中如果已经导入过的文件再次被重新导入时候，python不会再重新解释一遍，
而是选择从内存中直接将原来导入的值拿来用。这就是单例模式了。

单例模式：一个对象
    
    
提示：
    如果以后存在一个单例模式的对象，可以先在此对象中放入一个值，然后再在其他的文件中导入该对象，通过对象再次讲值获取到。
"""