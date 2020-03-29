import os,signal
print(os.getcwd())   #打印当前文件所在路径

print(os.listdir())  #打印当前文件所在文件夹里的所有文件名称

print(os.getenv('HOME'))
print(os.name)
print(os.stat('OS模块.py'))



print(signal.Signals)
