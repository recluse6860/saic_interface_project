#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import logging

class saic_redis():

    def __init__(self):
        
        self.Log = logging.getLogger('interface.redis')     
        self.Log.info(u'Init Redis Object')   
        
    def ConnectRedis(self):
        
        self.redishost = '10.32.140.82'
        self.redisport = 6800
        self.redisdb = 12
        
        self.Log.info('RedisHost %s', self.redishost) 
        self.Log.info('RedisPort %s', self.redisport)
        self.Log.info('RedisDB %s', self.redisdb) 
        
        redisconn = redis.StrictRedis(host = self.redishost, port = self.redisport, db = self.redisdb)
        
        self.Log.info(redisconn.ping())
        
        return redisconn
    
    def DisconnectRedis(self, redisconn):
        
        redisconn.connection_pool.disconnect()
        
    def Redis_Hget(self, name, key):
        
        HgetResult = self.redisconn.hget(name, key)
        return HgetResult     
