import requests

class APItool(object):



    def __init__(self,url,data,header,type):
        self.url=url
        self.data=data
        self.header=header
        self.type=type


    def getResp(self,type):
        if(type=='post'):
            resp = requests.post(url=self.url, data=self.data,headers=self.header)
        if(type=='get'):
            resp = requests.get(url=self.url)

        return resp
