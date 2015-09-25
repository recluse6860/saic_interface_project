#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import subprocess
import time
import psutil


class Venus:
    
    def __init__(self):
        
        self.Log = logging.getLogger('interface.venus')     
        self.Log.info(u'Init Venus Object')       
    
    def DeleteVenusConfig(self):
    
        """Delete Old Venus Config"""
        self.Log.info(u'========Delete Old Venus Config========')
        self.HOMEDIR = os.path.split(os.path.realpath(__file__))[0]     
        self.VenusDIR = os.path.split(self.HOMEDIR)[0] + "\\venus-http-adaptor"         
#         os.chdir("D:\\Saic_Interface_Project\\venus-http-adaptor")
        os.chdir(self.VenusDIR)
#         FileExist = os.path.isfile("D:\\Saic_Interface_Project\\venus-http-adaptor\\application.properties")
        FileExist = os.path.isfile(self.VenusDIR + "\\application.properties")
        if FileExist:
            self.Log.info(u'old application.properties file exist, remove it')   
            os.remove("application.properties")
        else:
            self.Log.info(u'application.properties file not exist')   
            pass
    
    
    def CreateVenusConfig(self):
        
        """Create New Venus Config"""
        self.Log.info(u'========Create New Venus Config========')    
        VenusAddress = "venus.service.ipAddressList = 10.32.140.83:16800\n"
        VenusConfig = "venus.socket.receiveBufferSize  = 64\nvenus.socket.sendBufferSize = 64"
        self.Log.info('VenusAddress %s', VenusAddress) 
        self.Log.info('VenusConfig %s', VenusConfig) 
        
        venus_file_object = open("application.properties",'a+')
        venus_file_object.write(VenusAddress)
        venus_file_object.write(VenusConfig)
        venus_file_object.close()
    
    def RunVenusAdaptor(self):
        
        """Run Venus Adaptor"""
        self.Log.info(u'========Run Venus Adaptor========')  
#         os.chdir("D:\\Saic_Interface_Project\\venus-http-adaptor\\bin")
        self.VenusRunDIR = self.VenusDIR + "\\bin"
        os.chdir(self.VenusRunDIR)
        print os.getpid()
        ProcessBat = subprocess.Popen("launcher.bat",creationflags=subprocess.CREATE_NEW_CONSOLE)
        print ProcessBat.pid
        time.sleep(15)
        return ProcessBat
        
    def CloseVenusAdaptor(self,ProcessBat):
        
        """Close Venus Adaptor""" 
        self.Log.info(u'========Close Venus Adaptor========') 
        ParentProcess = psutil.Process(ProcessBat.pid)
        ChildrenProcess = ParentProcess.children(recursive=True)
        for ChildProcess in ChildrenProcess:
            self.Log.info(u'Close child process') 
            ChildProcess.kill()
        psutil.wait_procs(ChildrenProcess, timeout=5)
        ParentProcess.kill()
        ParentProcess.wait(10)    
    