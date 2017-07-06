# -*- coding: utf-8 -*-
import requests
from urllib.request import urlretrieve
import json
import random
import xlrd
import xlwt
s = requests.Session()


#商户列表
comlist = 'http://xxx.com'
#登陆页
urllogin = 'http://xxx.com/Login.do'
#消费页
urllist = 'http://xxx.com/list.do'

class catxls():
    headers = {
          'Accept':'application/json, text/javascript, */*; q=0.01',
          'Accept-Encoding':'gzip, deflate',
          'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
          'Connection':'keep-alive',
          'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
          'Host':'xxx.com',
          'Origin':'http://xxx.com',
          'Referer':'http://xxx.com/agent/ims/tranLsH/init.do',
          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
          'X-Requested-With':'XMLHttpRequest'
        }
    
    def __init__(self):
        self.session = requests.Session()
        
        #pass
    #设置头
    def setheader(self,headers):
        self.headers = dict(self.headers,**headers)
    #登陆
    def login(self,url,logindata):
        self.session.post(urllogin,data=logindata)
    
    
    
    #验证码
    def getverify(self,url):
        picstr = self.session.get(url)
        f = open('code.jpg','wb')
        f.write(picstr.content)
        f.close()
    #输入验证码
    def putverify(self):
        self.verify = input('请输入验证码：')
    
    #取得商户列表
    def catchcom(self,url):
        pass
    #取得消费列表
    def catchfee(self,url,data,headers):
        pass
headers = {
          'Accept':'application/json, text/javascript, */*; q=0.01',
          'Accept-Encoding':'gzip, deflate',
          'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
          'Connection':'keep-alive',
          'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',

          'Host':'s.ruiyinxin.com',
          'Origin':'xxx.com',
          'Referer':'http://xxx.com/agent/ims/tranLsH/init.do',
          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
          'X-Requested-With':'XMLHttpRequest'
        }
url = 'http://xxx.com/agent/'
#requests.get(url)
postdata = {'loginname':'00001111',
            'password':'6e9729a91870fb57ce90fa19e1734656256374a'}
picurl = 'http://xxx.com/code.do?t='+str(random.random())

x = s.get(picurl)
f = open('x.jpg','wb')
f.write(x.content)
f.close()
#urlretrieve(picurl,'code.jpg')

mycode = input('输入验证码：')
postdata['code'] = mycode
urllogin = 'http://xxx.com/checkLogin.do'
#print(postdata)
x = s.post(urllogin,data=postdata,headers=headers)
#print(x.text)

#s.get(url+'login.do')
url1 = 'http://xxx.com/list.do'
x = s.post(url1,data={'page':1,'rows':100})
shops = json.loads(x.content)
shoparr = []
num = 1
for shop in shops['rows']:
    shoparr.append(shop['merId'])
    
print(shoparr)
urllist = 'http://xxx.com/list.do'
pdata = {
        
        's_referNo':'',
        's_serialNum':'',
        's_cardNo':'',
        's_tranType':'',
        's_tranStatus':'',
        's_tranDates':'20160601',
        's_tranDatee':'20170704',
        'page':1,
        'rows':100
        
        }


x = s.post(urllist,data=pdata,headers=headers)
content = x.text
s = json.loads(content)
for data in s['rows']:
    print(data['tranDate'])
