import logging
from Log import Log
from Venus import Venus
import json
 
Log = Log()
module_logger = logging.getLogger("interface.Temp1")  
module_logger.info(u'temo1 log')
 
Venus = Venus()
Venus.DeleteVenusConfig()
Venus.CreateVenusConfig()
ProcessBat = Venus.RunVenusAdaptor()
 
import redis
redishost = '10.32.140.82'
redisport = 6800
redisdb = 12
 
redisconn = redis.StrictRedis(host = redishost, port = redisport, db = redisdb)
print redisconn.ping()
 
print redisconn.info('server')
print redisconn.hget('mdse_stock', '5280')
redis_stock = redisconn.hget('mdse_stock', '5280')
print redisconn.connection_pool.disconnect()
redisconn.connection_pool.disconnect()
 
import requests
 
TestSesssion = requests.Session()
TestCookies = {}
TestPayLoad = {}
Timeout = 30
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0',
    'content-encoding': 'gzip',
    'content-type': 'application/json'
}
 
LocalAddress = 'http://127.0.0.1:8080/'
ServiceName = 'services/StockService/'
MethodName = 'queryStockRedis'
 
RequestUrl = LocalAddress + ServiceName + MethodName
RequestStaticJson = {"skuchnId":5280,
                     "realFlag":False}
 
RequestDynamicJson = {}
 
Result = TestSesssion.post(RequestUrl, data = json.dumps(RequestStaticJson), headers=headers)
 
 
 
 
 
print Result.headers
LoginCookie = Result.cookies
print Result.status_code
PageContent = Result.content
print PageContent
 
Venus.CloseVenusAdaptor(ProcessBat)
 
  