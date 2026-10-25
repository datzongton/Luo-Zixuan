# -*- coding: utf-8 -*-
#1,2,3,4组成互不相同且无重复数字三位数
lst=[]
n=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            tmp=100*i+10*j+k
            if i!=j and j!=k and i!=k:
                lst.append(tmp)
                n+=1
print(n)
print(lst)