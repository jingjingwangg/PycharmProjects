#coding:utf-8
from xml.dom import minidom
class readdata(object):
    def readtestdata(self,filename,firstcode,num,secondcode):
    ##parse为打开。使用mindom打开数据文件，通过相对路径获取文件地址，该模块为通用模块，文件名不能写死，文件名用参数接收
       root=minidom.parse("../readdate/"+filename)
       OneNode=root.getElementsByTagName(firstcode)[0]
       TwoNode=OneNode.getElementsByTagName(secondcode)[0].childNodes[0].nodeValue
       return TwoNode
