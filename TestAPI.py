from  common.APItool import *


url='http://localhost:8080/test/hello'
data={}
header={}
type='get'
apitool=APItool(url=url,data=data,header=header,type=type)
print(apitool.getResp(type))

