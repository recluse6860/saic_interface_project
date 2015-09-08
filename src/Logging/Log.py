#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import datetime
         
class Log:
    
    def __init__(self):    
               
        self.LOGDIR = os.path.join("D:\\Saic_Interface_Project",'Log')
        self.LOGFILE = datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.log'
        
        self.fileLog = logging.FileHandler(os.path.join(self.LOGDIR,self.LOGFILE),'w')
        self.streamLog = logging.StreamHandler()
        
        logging.basicConfig(level=logging.DEBUG,
                            format='',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename = os.path.join(self.LOGDIR, self.LOGFILE),
                            filemode='a'
                            )
        
        fileformatter = logging.Formatter('%(asctime)s %(name)s:%(levelname)s %(message)s')
        streamformatter = logging.Formatter('%(asctime)s %(name)s:%(levelname)s %(message)s')
        self.fileLog.setFormatter(fileformatter)
        self.streamLog.setFormatter(streamformatter) 
        logger = logging.getLogger('interface')
        logger.addHandler(self.fileLog)
        logger.addHandler(self.streamLog)
        logger.setLevel(logging.DEBUG)
        logger.info(u'Log file create')             
        
    def getLog(self, getLogName):
        
        logger = logging.getLogger(getLogName)
        logger.addHandler(self.fileLog)
        logger.addHandler(self.streamLog)
        logger.setLevel(logging.DEBUG)
        logger.info(u'Get Logger')
        return logger
        