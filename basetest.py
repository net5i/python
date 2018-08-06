# coding:utf-8

def lines(tp,num,title):
    def dot(func):
        def wap(*arg,**kargs):
            print(tp*20,title,tp*num)
            return func(*arg,**kargs)
        return wap
    return dot

# 9*9表

@lines(tp='-',num=100,title="这里是乘法表")
def maths(num=9):
    num = num+1
    for i in range(1,num):
        print('|',end='')
        for j in range(1,i+1):
            strs = strs = str(j) + '*' + str(i)+'='+str(i*j)
            if len(str(i*j))<2:
                    strs = strs + ' '
            if j==i:
                
                print(strs,'|')
            else:
                print(strs,'|',end=" ")
            
        print('-'*130)
            
# 闪电
num = 8
for i in range(1,num):
    print(' '*(num-i),end="")
    print(" *"*i)
for i in range(1,8):
    print(' '*7,end='')
    print(' *'*(8-i))


#三角
@lines(tp='-',num=100,title='这里三角形')
def sanjiao(num=8):
    num = num+1
    for i in range(1,num):
        print('%s%s%s' % (' '*(num-i-1),'*',' *'*(i-1)))
    for i in range(1,num-1):
        print('%s%s' % (' '*(i-1),' *'*(num-i-1)))
        

sanjiao(7)
maths()
