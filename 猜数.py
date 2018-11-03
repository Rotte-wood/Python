import random
import os
import time
b=6
print("Now that the guessing process begins,you have six chances！\n")
print("---------Start--------\n")
a=random.randint(1,100)
os.system("color 0a")
while (1):
    b-=1
    c=input("Please the enter：")
    if int(c)==int(a):
        print("Ok!You guess right!\n")
        break
    if int(c)<int(a):
        print("Sorry ,it's small！You have %d chace"%b)
    if int(c)>int(a):
        print("Sorry,it's big！You have %d chance"%b)
    if int(b)==0:
        print("-----------------------\n")
        print("Sorry,you havn't chance!\nI'm very sorry!\n")
        print("-----------------------\n")
        print("Random:%d\n"%a)
        break
os.system("pause")
