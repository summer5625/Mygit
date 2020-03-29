import logging

from conf import setting

log_name = setting.LOG_NAME                                                          # 获取日志名称

def logs(log_type):

    logger = logging.getLogger(log_type)                                             # 生成日志对象

    logger.handlers.clear()                                                          # 每次调用清空handlers列表
    logger.setLevel(logging.INFO)                                                    # 设置日志级别
    log_path = r'%s\log\%s' % (setting.FILE_PATH,log_name[log_type])                 # 设置日志存储路径
    fh = logging.FileHandler(log_path,encoding='utf-8')                              # 设置文件日志保存方式
    logger.addHandler(fh)
    file_formatter = logging.Formatter('%(asctime)s  %(levelname)s  %(message)s',
                                       datefmt='%Y-%m-%d %I:%M:%S %p'
                                       )                                             # 设置日志格式
    fh.setFormatter(file_formatter)

    return logger

