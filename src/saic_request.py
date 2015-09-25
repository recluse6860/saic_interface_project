#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import string

class saic_request():
    
    def __init__(self):
        
        self.Timeout = 30
        self.headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0',
                        'content-encoding': 'gzip',
                        'content-type': 'application/json'
                        }
        self.LocalAddress = "http://127.0.0.1:8080/services/"
        self.session = requests.Session()
        
    def Post(self, Param_Service_Name , Param_Service_Method, Param_Data):
        
        ParamUrl = self.LocalAddress + Param_Service_Name + Param_Service_Method
        Param_Json_Data = json.dumps(Param_Data)
        Response =  self.session.post(url = ParamUrl, data = Param_Json_Data, headers = self.headers)
        ResponseStatusCode = Response.status_code
        if ResponseStatusCode == (requests.codes.ok):
            ResponseJson = Response.content.replace('\"','\\"')
            ResponseJson = ResponseJson.replace('\'','\"')
            ResponseErrorCode = json.loads(ResponseJson)['errorCode']
            ResponseResult = json.loads(ResponseJson)['result']
        else:
            ResponseErrorCode = ()
            ResponseResult = []
        ResponseList = [ResponseStatusCode, ResponseErrorCode, ResponseResult]
        
        return ResponseList
    
    def Get(self, Param_Service_Name,  Param_Service_Method):
        
        ParamUrl = self.LocalAddress + Param_Service_Method
        Response =  self.session.get(url = ParamUrl)
        
        return Response
        