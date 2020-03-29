import logging
from logging import handlers  #导入日志截断模块


#创建fillter对象
class IgnoreBackupFilter(logging.Filter):
    def filter(self, record):
        return 'db backup' not in record.getMessage()   #将日志中带db backup的日志忽略掉


#生成 logger 对象

logger = logging.getLogger('web')

#把filtter对象添加到logger中

logger.addFilter(IgnoreBackupFilter())

#设置日志级别
logger.setLevel(logging.DEBUG)

#生成 handler 对象

ch = logging.StreamHandler()                 # 输出日志到屏幕
fh = logging.FileHandler('web.log')          # 输出日志到文件中

#截取日志，按照每份日志的大小来保存，超出大小后重新生成新的日志
fh1 = handlers.RotatingFileHandler('web.log',maxBytes=10,backupCount=3) #(日志名称，没份日志大小，保存多少份日志）

#截取日志，按照时间来截取日志
fh2 = handlers.TimedRotatingFileHandler('web.log',when='s',interval= 2,backupCount=3)  #(名称，时间级数，时间长度，保存文件个数）

#设置输出日志的级别

ch.setLevel(logging.INFO)
fh.setLevel(logging.WARNING)

#把handler对象绑定到logger

logger.addHandler(ch)
logger.addHandler(fh)

#生成 formatter 对象
# 把formatter 对象绑定handler对象


file_formatter = logging.Formatter('%(asctime)s - %(levelno)s - %(filename)s  - %(message)s',
                                    datefmt='%Y-%m-%d %I:%M:%S %p')
console_formatter = logging.Formatter('%(asctime)s - %(levelno)s - %(filename)s  - %(message)s - %(lineno)d',
                                      datefmt='%Y-%m-%d %I:%M:%S %p')

ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)

logger.debug('love you')
logger.info('you love?')
logger.warning('Yes you love')
logger.debug('db backup not love')
