import os
import time
import random

class ks:
    #x范围
    x = (700,900)
    #y范围
    y = (900,1600)
    #滑动幅度
    z = (400,700)

    #执行滑动语句
    adbexec = "adb -s {machine} shell {action}"
    #计时器，主要用于检测设备在线情况
    count = time.time()

    def __init__(self):
        #取得设备列表
        self.getMachineList()

        while(True):
            point = self.makePoint()
            #滑动时间
            times = self.makeNum(50,450)
            self.swipe(point,times)
            machine = random.choice(self.machineBox)
            strs = self.adbexec.format(machine = machine,action = self.executeStr)

            #判断时间，主要用于监测连接的设备
            if time.time() - self.count > 10:
                count = time.time()
                self.getMachineList()

            #print(strs)
            os.system(strs)
            #执行完后暂停
            self.sleep(random.randint(1,8))

    '''
    创建随机数
    '''
    def makeNum(self,x,y):
        return random.randrange(x,y)


    '''
    创建点
    '''
    def makePoint(self):
        x1 = self.makeNum(self.x[0],self.x[1])
        y1 = self.makeNum(self.y[0],self.y[1])
        x2 = self.makeNum(self.x[0],self.x[1])
        y2 = y1 - self.makeNum(self.z[0],self.z[1])
        return x1,y1,x2,y2

    '''
    休眠时间
    '''
    def sleep(self,times):
        time.sleep(times)

    #滑动操作
    def swipe(self,point,times=None):
        notime = "input swipe {x1} {y1} {x2} {y2}".format(x1=point[0], y1=point[1], x2=point[2], y2=point[3])
        hatime = "input swipe {x1} {y1} {x2} {y2} {times}".format(x1=point[0], y1=point[1], x2=point[2], y2=point[3],
                                                                  times=times)

        #得到应该执行的语句
        self.executeStr = hatime if isinstance(times,int) else notime


    '''
    取得连接设备列表
    '''
    def getMachineList(self):
        machineBox = []
        machines = os.popen("adb devices")
        machineList = machines.readlines();

        for i in machineList:
            catchMathine = i.find('\tdevice')
            if(catchMathine != -1):
                machineBox.append(i.split('\t')[0])

        self.machineBox = machineBox


if __name__ == '__main__':

    ks = ks()




