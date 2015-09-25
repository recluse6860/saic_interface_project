#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import json
from Log import Log
from Venus import Venus
from saic_redis import saic_redis
from saic_request import saic_request
from nose.tools import *

def setUpModule():
     
    global Venus
    global ProcessBat
    global Log
 
    Log = Log()
    module_logger = logging.getLogger("interface.PayMdm")  
    module_logger.info(u'PayMdm Setup') 
    Venus = Venus()
    Venus.DeleteVenusConfig()
    Venus.CreateVenusConfig()
    ProcessBat = Venus.RunVenusAdaptor()
  
def tearDownModule():
 
    Venus.CloseVenusAdaptor(ProcessBat)    
     
class Test_StockService:
    
    @classmethod
    def setUpClass(self):
        
        global Redis
        global RedisConn
        Redis = saic_redis()
        RedisConn = Redis.ConnectRedis()
        return RedisConn
        
    @classmethod
    def tearDownClass(self):
        
        Redis.DisconnectRedis(RedisConn)
 
    def Test_QueryStockRedis(self):
        def_logger = logging.getLogger("interface.StockService.QueryStockRedis")  
        def_logger.info(u'StockService.QueryStockRedis start')
        
        self.RedisStock = RedisConn.hget('mdse_stock', '5280')
        def_logger.info('Redis stock is ' + self.RedisStock)
        
        Request_Json = {"skuchnId":5280,
                        "realFlag":False}
        request = saic_request()
        
        Service_Name = 'StockService/'
        QueryStockRedis_Result = request.Post(Service_Name, 'queryStockRedis' ,Request_Json)
        
        def_logger.info('request status is %s', QueryStockRedis_Result[0])
        def_logger.info('venus error code %s', QueryStockRedis_Result[1])
        def_logger.info('venus msg is %s', QueryStockRedis_Result[2])
        
        StockInfo = json.loads(QueryStockRedis_Result[2])
        StockInfo = StockInfo["map"]["5280"]
               
        eq_(self.RedisStock, StockInfo, msg="interface stock is not equal redis stock") 
        
 
class Test_CreditSearchService:
 
 
    def Test_QueryBalance(self):

        def_logger = logging.getLogger("interface.CreditSearchService.QueryBalance")  
        def_logger.info(u'CreditSearchService.QueryBalance start')

        Request_Json = {
                        "balanceQueryDto": {
                        "userId": 560141,
                        "agencyNo": "CX"
                        }
                    }
        request = saic_request()
        
        Service_Name = 'CreditSearchService/'
        QueryBalance_Result = request.Post(Service_Name, 'queryBalance' ,Request_Json)
        def_logger.info(u'dddddddddd')

               
        eq_(55, 44, msg="interface stock is not equal redis stock") 

