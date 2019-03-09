import logging
import time
import os

class Logger(object):
    def __init__(self,logger):

        #创建一个logger对象
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))

        log_path= os.path.dirname(os.path.abspath('.'))+'/logs/'
        log_name=log_path+rq+".log"
        #创建headdler用于日志的输出
        #文件输出
        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        #控制台输出
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getLog(self):
        return self.logger

