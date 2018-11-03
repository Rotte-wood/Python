import random
import os
import time
b=6
print("现在猜数开始,您共有6次机会！\n")
print("---------分割线--------\n")
a=random.randint(1,100)#生成随机数函数:random.randint(a,b),'import random'
os.system("color 0a")
while (1):
    b-=1
    c=input("请输入：")
    if int(c)==int(a):
        print("恭喜您！猜对了\n")
        break
    if int(c)<int(a):
        print("对不起,猜小了！您还有%d次机会"%b)
    if int(c)>int(a):
        print("对不起，猜大了！您还有%d次机会"%b)
    if int(b)==0:
        print("-----------------------\n")
        print("对不起，您没有机会了\n电脑将会在90秒内关机\n我叫陈贱贱!\nI'm very sorry!\n")
        print("-----------------------\n")
        print("随机数为:%d\n"%a)
        print("-----------------------\n")
        print("关机取消:[打开运行]输入[cmd]:\nshutdown -a")
        time.sleep(5)
        os.system("shutdown -s -c 惊不惊喜？意不意外？我叫陈贱贱,认识一下呗!*.*")
        break
os.system("pause")
