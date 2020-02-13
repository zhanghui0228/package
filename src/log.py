import os
import os.path
import logging
from datetime import datetime


class Log(object):
    tag = 'log'
    log_path = '/tmp/huilog'
    if os.path.exists(log_path) == False:
        os.mkdir(log_path)
    NowDate = datetime.now().date()
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    LogName = os.path.join(log_path, "{log_name}").format(log_name=NowDate)
    logging.basicConfig(filename=LogName, level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    
    def __init__(self, context, other=None):
        self.context = context
        self.other = other

    def Info(self):
        """info log """
        logging.info('INFO {other}-{context}'.format(context=self.context, other=self.other))

    def Err(self):
        """error log"""
        logging.error('ERR {other}-{context}'.format(context=self.context, other=self.other))

    def Warn(self):
        """warning log"""
        logging.warning('WARNING {other}-{context}'.format(context=self.context, other=self.other))


def log(context, other=None):
    """log实例化，进行引用"""
    run = Log(context, other)
    try:
        run.Info()
    except:
        run.Err()


def help():
    context = """
	功能：
		目前只支持输出日志的level ：info、error、warning
	运行方法：log(context, other)
            context : 输出到日志中的内容， 可以是执行的结果
            other ：自定义输出到日志的内容，可以是执行的命令
"""
    print(context)
