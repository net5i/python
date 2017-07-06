# -*- coding: utf-8 -*-
import requests
from urllib.request import urlretrieve
import json
import random
import xlrd
import xlwt
s = requests.Session()


#商户列表
comlist = 'http://xxxx.com'
#登陆页
urllogin = 'http://xxxx.com/login.do'
#消费页
urllist = 'http://xxxx.com/list.do'

class catxls():
    headers = {
          'Accept':'application/json, text/javascript, */*; q=0.01',
          'Accept-Encoding':'gzip, deflate',
          'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
          'Connection':'keep-alive',
          'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
          'Host':'s.ruiyinxin.com',
          'Origin':'http://s.ruiyinxin.com',
          'Referer':'http://s.ruiyinxin.com/agent/ims/tranLsH/init.do',
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
        self.verify = input('请输入验证码：')
    #输入验证码
    def putverify(self):
        self.verify = input('请输入验证码：')
    
    #取得商户列表
    def catchcom(self,url):
        data = self.session.post(url,data={'page':1,'rows':100})
        return data.content.decode('utf-8')
    #取得消费列表
    def catchfee(self,url,data,headers = {}):
        data = self.session.post(url,data)
        return data.content.decode('utf-8')

#有用的字段
fieldslist = [
'bankCardName', #身份证
'bankCard',#身份证号
'merName',#商户名
'parentMccName',#商户类型
'createTime',#申请时间
'finalAuditTime',#终审时间
'finalAuditPersonName',#审核人员
'contactPhone',#联系电话
'merId'#商户编号
]
cls = catxls()
cls.getverify('http://s.ruiyinxin.com/agent/img/code.do?t='+str(random.random()))
logindata = {'loginname':'00001111',
            'password':'6e9729a91870fb57ce90fa19e1734656256374a',
            'code':cls.verify
            }
cls.login(urllogin,logindata)


merId = []
mer = []
comlists = cls.catchcom(comlist)
comlists = json.loads(comlists)['rows']
for i in comlists:
    merId.append(i['merId'])
    mer.append([i['merId'],i['bankCardName']])

pdata = {
        
        's_tranDates':'20160601',
        's_tranDatee':'20170704',
        'page':1,
        'rows':100
        
        }



feelists = []
for i in merId:
    pdata['s_merId'] = i
   
    x = cls.catchfee(urllist,pdata)
    feelists.append(json.loads(x)['rows'])


slx = xlwt.Workbook()
wlx = slx.add_sheet('abc')
col = 0

print(mer)
#row = 0
for com in feelists:
    
    names = ''
    for feelists in com:
        for mers in mer:
            if feelists['merId'] == mers[0]:
                names = mers[1]
        row = 0
        for im in feelists:
            #print(str(col) + '-' + str(row) + '-' + str(im))
            wlx.write(col,row,feelists[im])
            row += 1
        wlx.write(col,row,names)
               
        col += 1
            
slx.save('fee3.xls')
#x = cls.catchfee(urllist,pdata)
#商户信息
#feelists = json.loads(x)['rows']
