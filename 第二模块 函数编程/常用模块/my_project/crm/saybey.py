import sys,os

BAS_DIR = os.path.abspath(__file__)  #获取文件当前在计算机中的绝对储存路径
print(BAS_DIR)
BAS_DIR = os.path.dirname(os.path.dirname(BAS_DIR))
print(BAS_DIR)
sys.path.append(BAS_DIR)   #将路径添加进导入模块的查找路径
def saybey(name):
    print('beybey',name)

